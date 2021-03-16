# Status Update in CMPSC 610
## March 15, 2021

In CS 600 (Fall 2020), I used a lot of the time to propose my senior thesis topic.
This semester (Spring 2021) in CS 610, I started the actual work mentioned in the
proposal. For my senior thesis, I planned to build a machine learning model to analyze
the impact of Skill-Biased Technological Change and globalization on income inequality
within high-income, upper-middle-income, and lower-middle-income countries. Last
semester, a lot of my work was figuring out the best machine learning model for
my analysis, making a list of the countries I will be performing the analysis on,
and most importantly, choosing the variables that influence income inequality,
SBTC, and Globalization. Based on the feedback I received from my first reader
for my proposal, I decided to work on all the areas that needed to be modified.

According to my first reader, my proposal needed a lot of improvement in the Method
of Approach section. I used my time to do extensive research on my machine learning
model: LASSO Regression. I was able to find research papers that justified why LASSO
regression is a better model than linear regression, primarily because it supports
regularization that helps with overfitting and variable selection. I showed a detailed
explanation in my third chapter by laying out the logistics of both the kinds of
regression and how LASSO outweighs the traditional linear regression model. I introduced
the models and explained how it functions to offer the type of analysis integral
to the project’s goal. The next step was to work on the justification of my variables.
I had chosen a set of twelve variables that affect SBTC and globalization. It was
vital for me to present a well-thought-out and meaningful discussion of the variables
for my study. I included research papers that have used those variables in their
analysis, which provided evidence for my selection. My first reader had also suggested
focusing on the project’s feasibility to make sure that I complete the thesis on time;
I decided it would be better to choose 12 countries rather than 40 countries. That
did save me a lot of time while I was extracting the required data from the World
Bank’s site, and I was also able to clean and organize my data correctly.

Since the last few weeks, I have spent ample time finishing my third chapter and
working on my Python code to get the desired results that will be discussed in my
fourth chapter, ‘Results and Discussion’. My model implementation in Python was
relatively simple because I used the SciKit-Learn library with a built-in LASSO
regression method. There were multiple challenges where my model was not showing
the results I had expected; instead, it was compounding the calculations for all
the countries rather than one specific country. Since my data is panel data, I had
to find a better way to work with the data. Fortunately, I found some valuable
resources on the internet that helped me solve the problem. I am currently working
on my results and discussion section, where I plan to have three sections that
focus on my results on high-income, upper-middle-income, and lower-middle-income
economies and explain the results. I have to run a couple more tests to identify
the critical variables in my model. On successful completion, my thesis will help
me identify those factors that play an important role in affecting income inequality.
Once I am done with the final implementation, I will present my findings in the
fourth chapter along with the conclusion.



​
