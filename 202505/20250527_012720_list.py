import pathlib
from icecream import ic
import json

md_line_content = ""
items = []

for filepath in pathlib.Path("./data").glob("**/*.json"):
    # ic(filepath)
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
        kernels = data["kernels"]

        for kernel in kernels:
            item = {
                "userName": kernel["author"]["userName"],
                "title": kernel["title"],
                "totalVotes": kernel["totalVotes"],
                "scriptUrl": kernel["scriptUrl"],
            }
            items.append(item)

            # md_line = f"""- [ ] [{title}](https://www.kaggle.com{scriptUrl}) - {userName}, {totalVotes} votes \n"""
            # md_line_content += md_line

            # dataSourceUrl = kernel["dataSources"][0]


items.sort(key=lambda item: item["totalVotes"], reverse=True)
# ic(items)

with open("kaggle_kernels.md", "w", encoding="utf-8") as file:
    md_line_content = ""
    for item in items:
        md_line_content += f"""- [ ] [{item['title']}](https://www.kaggle.com{item['scriptUrl']}) - {item['userName']}, `{item['totalVotes']}` votes \n"""

    file.write(md_line_content)
    pass
