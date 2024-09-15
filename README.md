The Main AIM of this project is to Recommend the movies Based on the content.

--> Basically this Recommender Systems can be of 3 types
    
    1. Content Based  --> It is purely based on the genres,Cast,Overview etc.. based recommendation System.
    2. Utility Based  --> It is type of mutual recommendation basis where two are friends and likes similar content if some one likes it based on which another will get recommended.
    3. Hybrid Based = Content + Utility --> It is combination of both the types.

    STARTING WITH PROJECT DESCRIPTION:

    > Initially importing all the packages used for the project like numpy and pandas
    > Next stage is accessing the data frame using the function named "pandas.read_CSV()".
    > Further datasets need to be merged using "merge()" function.
    > After merging of the datasets choose the required attributes among all the attributes provided for recommendation purpose.
    > make all them into a single list.
    > After replacing the data set with only required attributes find the null values and any Outlier values.
    
    DATA PREPROCESSING STAGE:

    > If any column consists of any sort of null values drop the whole row if the count is less.
    > If the count is more use another preprocessing techniques like binning methods like replace the value with Mode, median or mean.
    > After which search for any duplicated values if so drop that particular column.
    > Next step is converting the list of dictionaries which contain strings that need to be converted to literals.
     
           where we take the help of "ast" library in python which is termed as "Abstract Syntax Tree" 
           - which contains the inbuilt function like "ast.literal_eval()".
           - where it converts the list of dictionaries of string to literals.

    > In order to get the code reference refer to movie-recommender-system.ipynb file. the name of the function is convert().
    
