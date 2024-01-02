from os import walk 
import calendar as cal


def article_gen(article_arg):
    article_folder = next(walk('articles/' + article_arg))[1]
    print(article_folder)

    article_list = []

    for article in article_folder:
        article_add = []
        article_add.append(article[0:3]) # Article Type
        article_add.append(article[3:7]) # Article Year
        article_add.append(article[7:9]) # Article Month
        article_add.append(article[9:11]) # Article Day
        article_add.append((article[11:].replace("_", " ")).title()) # Article Name
        
        article_list.append(article_add)
    
    return article_list

article_test = article_gen('art')

for article in article_test:
    print(
        article[4] + 
        " was made on " + 
        cal.month_name[int(article[2])] + 
        " " + article[3] + ", " + article[1] + 
        " and is a " + article[0] +
        " project."
    )
