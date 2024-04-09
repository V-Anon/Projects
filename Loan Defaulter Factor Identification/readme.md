# Loan Default 
> An attempt to use Exploratory Data Analysis techniques to identify the driving variables which are strong indicators that applicants of a loan has high chance to become defaulters. 

## Summary
The data set as well as data dictionary were collected and processed with necessary data cleaning steps. Non-impacting features were removed through this process and the rest of the features were analysed using Univariate, Bivariate, Segmented and Multivariate analysis. After each analysis, features those weren’t having significant influence of defaulter ratio were removed consecutively. From 115 potential features in the given dataset 7 driver variables that indicates possibility of loan default was identified and they were annual _inc, funded_amnt_inv, int_rate, term, grade, purpose,  and addr_state.


<!-- You don't have to answer all the questions - just the ones relevant to your project. -->

<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Business Understanding
- The business objective is to identify the risky loan applicants who are potential Defaults , and therefore  reducing sanctioning such loans so as to cut down the credit loss. These driving factors can be used for portfolio and risk assessment by the company.
- There are Two Types of Risks: 
a) Not sanctioning the loan when the applicant can repay, and hence loss of business.
b) Sanctioning the loan when applicant can’t repay and hence, financial loss.
- The scope of the project is to minimize only second type risk.
- Two Types of Decision taken : a) Loan Accepted and b) Loan Rejected
- Loan Rejected means no transactional history of applicants  hence its out of scope for this analysis.
- Three loan statuses: Fully Paid – Applicant fully paid the loan, Charged Off – Applicant has not paid the loan and loan is default, Current – Applicant in process of paying instalment.
- Current status loans are excluded as they can’t provide insight for the defined scope of project.

## Conclusions
Driver Variables that decide whether a loan will become default or not are
- annual _inc
- funded_amnt_inv
- int_rate
- term
- grade
- purpose
- addr_state

<!-- As the libraries versions keep on changing, it is recommended to mention the version of library used in this project -->





<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->

