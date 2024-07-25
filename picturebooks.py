import re
from inspect_ai import Task, task
from inspect_ai.model import ChatMessageSystem, ChatMessageUser, ContentImage, ContentText
from inspect_ai.scorer import Score, Target, accuracy, scorer, CORRECT, INCORRECT
from inspect_ai.solver import (
  chain_of_thought, generate, TaskState
)
from inspect_ai.dataset import Sample, json_dataset

def extract_after_last_answer(s):
    keyword = "ANSWER"
    last_occurrence = s.rfind(keyword)
    if last_occurrence == -1:
        keyword = ":"
        last_occurrence = s.rfind(keyword)
        if last_occurrence == -1:
            return s  # Return the entire string if neither ANSWER nor a colon is present
    return s[last_occurrence + len(keyword):]

def extract_last_set(input_string):
    # Regular expression to match sets in Python format
    pattern = re.compile(r'\{[^{}]*\}')
    matches = pattern.findall(input_string)
    return matches[-1] if matches else ""

import base64

def image_to_base64_data_url(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Determine mime type of the image
    mime_type = None
    if image_path.lower().endswith('.jpg') or image_path.lower().endswith('.jpeg'):
        mime_type = 'image/jpeg'
    elif image_path.lower().endswith('.png'):
        mime_type = 'image/png'
    elif image_path.lower().endswith('.gif'):
        mime_type = 'image/gif'
    elif image_path.lower().endswith('.bmp'):
        mime_type = 'image/bmp'
    else:
        raise ValueError('Unsupported image format')
    
    data_url = f'data:{mime_type};base64,{encoded_string}'
    
    return data_url

def jaccard_index(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    
    if union == 0:
        return 1.0
    
    return intersection / union

def record_to_sample(record):
    objects = str(record["correct"] + record["incorrect"])[1:-1]
    system_prompt = f"For the following task, it is important that you answer with 'ANSWER:' followed by a subset of the words {objects}, also as list of words separated by commas."
    prompt = f"In the image, you can see an open picture book. There are holes in its cover. On the first page, there are pictures of objects. Which pictures are visible when the book is closed?"

    return Sample(
        input=[ChatMessageSystem(content=[ContentText(text=system_prompt)]),
               ChatMessageUser(content = [
                ContentText(text=prompt),
                ContentImage(image=record["image"])
            ])],
        target=str(set(record["correct"])),
        id=record["id"]
    )

dataset = json_dataset("puzzles/plants.jsonl", record_to_sample)

@scorer(metrics={
        "setequal": [accuracy()],
        "jaccard": [accuracy()]
    })
def setcompare():
    async def score(state: TaskState, target: Target):
        answer = extract_after_last_answer(state.output.completion)
        translation = str.maketrans('', '', '{}"\'[]: ')
        answer = answer.translate(translation).strip().split(",")
        target = target.text
        target = target.translate(translation).strip().split(",")
        answer = set(answer)
        target = set(target)

        return Score(
            value  = {"setequal": CORRECT if target == answer else INCORRECT,
                      "jaccard": jaccard_index(target, answer)},
            answer = str(answer)
        )

    return score

@task
def picturebooks():
    return Task(
        dataset=dataset,
        plan=[
          chain_of_thought(),
          generate()
        ],
        scorer=setcompare(),
    )