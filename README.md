

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="220" height="80">
  </a>

  <h3 align="center">Senior Thesis</h3>

  <p align="center">
    Quest for an Acceptable Level of Income Inequality: A Comparative Analysis of Implications of Skill-Biased Technological Change and Globalization between High-Income, Upper-Middle-Income, and Lower-Middle-Income Coutries
    <br />
   
    <br />
    Quest for an Acceptable Level ofIncome Inequality: A Comparative Analysis of Implications ofSkill-Biased Technological Change andGlobalization between High-Income, Upper-Middle-Income, and Lower-Middle-Income Coutries
    <br />
    
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#project-overview">Project Overview</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- PROJECT OVERVIEW -->
## Project Overview

This project comprises of the senior thesis presented to the Department of Computer Science at Allegheny College. It includes the implementation of a machine learning model, 'LASSO' (Least Absolute Shrinkage and Selection Operator) regression, to study the impact of Skill-Biased Technological Change on Income Inequality within High-Income Countries (HICs), Upper-Middle Income Countries (UMICs), and Lower-Middle-Income Countries (LMICs).

In today's time, technology has become embedded in our day-to-day activities and businesses. Emerging technologies, including artificial intelligence, machine learning, and advanced robotics, can automate many tasks currently performed by workers, leading us to a quiet revolution, the Automation Revolution
.Automation in infrastructure and development is no longer a luxury but rather a necessity for humankind to thrive. Globalization, on the other hand, has helped integrate economies around the world. However, as countries continue to climb the ladder of development, the level of income inequality which increases with economic growth continues to spike. It poses the question of how much inequality is appropriate, and what effect does the widening discrepancy between rich and poor people around the world have on economic development and prosperity? This project aims to shed light on this issue by conducting a panel-data study of twelve countries to determine the important variables that influence their economic growth and how those factors relate to Skill-Biased Technological Change (SBTC) and Globalization. The evaluation is carried out using a LASSO-based regression analysis, with GDP per capita growth (an indirect indicator of income inequality) as the dependent variable and factors affecting SBTC and globalization as the independent variables.  

### LASSO Regression

LASSO Regression (Least Absolute Shrinkage and Selection Operator) is a regression analysis method built on the principle of a linear regression model. What sets it apart from the standardized regression model is that it performs variable selection and regularization (prevents overfitting), the primary reasons for choosing this model. One of the model’s primary goals is to obtain a subset of accurate predictor variables (or independent variables) and hence enhance the prediction accuracy for the model. 

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started:
**To avoid retyping too much info. Do a search and replace with your text editor for the following:**
`github_username`, `repo_name`, `twitter_handle`, `email`, `project_title`, `project_description`



### Built With

* [Python3](https://www.python.org/)
* Libraries in Python:
  * [Pandas](https://pandas.pydata.org/)
  * [NumPy](https://numpy.org/)
  * [Matplotlib](https://matplotlib.org/)
  * [scikit-learn](https://scikit-learn.org/stable/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Installing `Python`
* [Download Python](https://www.python.org/downloads/)
 

### Installation 

1. Clone the repository
   ```sh
   git clone git@github.com:Allegheny-Computer-Science-600-F2020/project04-thesis-rauniyars.git
   ```
2. Install `pandas` library
   ```sh
   pip install pandas
   ```
The libraries `NumPy`, `Matplotlib`, and `sci-kit learn`, have been accessed by using the `import` statements in the python files in the `src` folder of the repository.

<!-- USAGE EXAMPLES -->
## Running the Program

The source code consists of two python files: `lasso.py` and `lambda.py`. The python file `lasso.py` contains the code for the implementation of the LASSO regression model. It also constitutes of code that generates the plots showing the value of coefficients of the independant variable for each of the countries. The second python file `lamda.py` constitutes of the code for the k-fold cross validation for the regularization parameter $\lambda. Upon succcessful installation of python3 and pandas, the files will run using the following commands:

* Command for running the file `lasso.py`
  ```sh
  python3 lasso.py
  ```
* Command for running the file `lasso.py`
  ```sh
  python3 lambda.py
  ```

_For more examples, please refer to the [Documentation](https://example.com)_




<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap 

See the [open issues](https://github.com/github_username/repo_name/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()


