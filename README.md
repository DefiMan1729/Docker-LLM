# Exposing LLM/GenAI based services as API 

This is a FastAPI application that uses the LangChain library and OpenAI to analyze employee feedback.

## Overview

The application uses the OpenAI API to generate language models, which are then used to analyze the feedback. The analysis involves three steps:

1. Summarizing the feedback.
2. Identifying the employee's weaknesses.
3. Providing an improvement plan based on the identified weaknesses.

The application is available via the following endpoint

## Usage

The application provides three endpoints:
- `/feedback/{feedback}`: Takes a string of feedback as input and returns a summary of the feedback, identified weaknesses, and a recommended improvement plan.

## Example

Here's how you can use the feedback endpoint:

```bash
curl -X GET "http://localhost:8000/feedback/{feedback}"
```
Replace `{feedback}` with the actual feedback string. The response will be a JSON object containing the summary, weaknesses, and recommendation.

## Explanation of the LLM code in main.py

1. **Summarizing the Feedback**: The first step involves summarizing the employee's performance review. This is done using a language model that has been trained on a variety of text data. The model takes the review as input and generates a concise summary. This is achieved by using a `ChatPromptTemplate` with the template "give me a summary of this employee's performance\n{review}". The output of this step is stored in 'review_summary'.

2. **Identifying Weaknesses**: The second step involves identifying the employee's weaknesses from the summarized review. This is also done using a language model. The model takes the summarized review as input and identifies key areas where the employee could improve. This is achieved by using a `ChatPromptTemplate` with the template "identify the employee's weaknesses\n {review_summary}". The output of this step is stored in 'weakness'.

3. **Providing an Improvement Plan**: The final step involves generating an improvement plan based on the identified weaknesses. Again, this is done using a language model. The model takes the identified weaknesses as input and generates a plan for how the employee can improve in these areas. This is achieved by using a `ChatPromptTemplate` with the template "provide an improvement plan for the employee based on\n {weakness}". The output of this step is stored in 'recommendation'.

These three steps are implemented as a sequence of LangChain models, each taking the output of the previous model as input, in a `SequentialChain`. When you provide feedback to the `/feedback/{feedback}` endpoint, it goes through these three steps and returns a JSON object containing the summary of the feedback, identified weaknesses, and a recommended improvement plan.
