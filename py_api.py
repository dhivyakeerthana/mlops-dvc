# import dvc.api
# with dvc.api.open("metrics.csv", repo="https://github.com/dhivyakeerthana/mlops") as f:
#     content = f.read()
#     print(content)

with open("metrics.csv") as f:
    content = f.read()
    print(content)
