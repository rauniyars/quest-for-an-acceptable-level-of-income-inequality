<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">project_title</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
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
.Automation in infrastructure and development is no longer a luxury but rather a necessity for humankind to thrive. Globalization, on the other hand, has helped integrate economies around the world. However, as countries continue to climb the ladder of development, the level of income inequality which increases with economic growth continues to spike. It raises the question: What level of inequality is acceptable, and what is the effect of this widening gap between the rich and low across the globe has on economic growth and prosperity? This project aims to spark light on this question by creating a panel-data analysis of twelve countries to assess the the significant indicators that affect their economic growth and how do those factors relate to Skill-Biased Technological Change (SBTC) and Globalization. The assessment is implemented by creating a LASSO-based regression analysis where we the GDP per capita growth (an indirect measure for Income Inequality) as our dependent variable and factors influencing SBTC and Globalization as our independent variables. With or proposed research, I wish to understand if what the current trends could cost to the future of the global economy.

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



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()


