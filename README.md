# Picturebooks
Which objects are visible through the holes in a picture book? This visual task is easy for adults, pretty doable for primary school children, but perhaps hard for current (July 2024) vision transformers.

The task in question is closely adapted from a problem for grades 3 and 4 of the international Kangoroo math event. It goes like this: "In the following image, you can see an open picture book. There are holes in its cover. On the first page, there are pictures of objects. Which pictures are visible when the book is closed?" We also give a list of the images to be chosen from, so in this case `"Avocado", "Ginger", "Kiwi", "Watermelon"`.

![ ](https://github.com/file-acomplaint/picturebooks/blob/main/puzzles/plants-34.png?raw=true)

And the correct answer here is "Watermelon, Ginger" (in any order). Let's see what GPT-4o has to say:

> To determine which pictures are visible when the book is closed, follow these steps: 1. Identify the position of the hole on the left side based on the grid layout. 2. Observe how this corresponds to the position of the objects on the right side. 3. Note which objects on the right side would align with the hole when the book is closed. Based on the grid in the image: - The hole on the left side spans the coordinates (1,2) to (3,6). - When the book is closed, the objects that align with this hole are in the corresponding positions on the right side, which are avocado, watermelon, and ginger. ANSWER: avocado, watermelon, ginger

Apparently, the problem was understood, and even the steps towards a solution make sense. But the spatial computation is not quite there. This repository contains code to generate more instances of the above problem, and as the scores below indicate, this solution attempt indicated a pattern across all those.  

### Scores
With a sample size of `n=50`, we obtain
|  | GPT-4o-mini |  GPT-4o-mini + Chain of Thought | GPT-4o | **GPT-4o + Chain of Thought** | Random Baseline |
| - | ----------- | -------------------------- | ------ | ------------------------- | -------------------|
| Accuracy | 0.02 |  0.04 | 0.08 | 0.12 | 0.04 |
| Jaccard | 0.44 | 0.43 | 0.38 | 0.45 | 0.2 | 

### How to run
This eval is implemented in the UK AI Safety Institute's [Inspect](https://inspect.ai-safety-institute.org.uk) framework. After installing that, you can do a test run with `inspect eval picturebooks --model openai/gpt-4o-mini --limit 1` in the main directory and remove the `limit` parameter to go through all samples.

### Heritage
Many thanks to the Kangoroo math competition team for the task idea. You can read an interview with mathematician Meike Akveld, in which the problem is featured, [here](https://johnian.joh.cam.ac.uk/news/career-spotlight-meike-akveld/).

### License
Code and images are the author's, and licensed under MIT.
