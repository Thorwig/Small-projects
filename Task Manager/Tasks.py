import pandas as pd
import os


class Tasks():

    def __init__(self):
        self.schema = {
            "Name": "string",
            "Status": "String",
            "Description": "string"
        }
        self.df = pd.DataFrame(columns=self.schema.keys())
        self.output_path = "output.csv"

    def create_task(self, name, short_description):
        created_data = {
            "Name": name,
            "Status": "New",
            "Description": short_description
        }

        df = pd.concat([self.df, pd.DataFrame(
            [created_data])], ignore_index=True)

        if os.path.exists(self.output_path):
            df.to_csv(self.output_path, mode='a', header=False, index=False)
        else:
            df.to_csv(self.output_path, mode='w', header=True, index=False)

    def show_tasks(self, filter):
        try:
            df = pd.read_csv("output.csv", sep=",")
            if filter == "New":
                print(df[df.Status == "New"].to_csv(sep='\t', index=False))

            elif filter == "In Progress":
                print(df[df.Status == "In Progress"].to_csv(
                    sep='\t', index=False))

            elif filter == "Finished":
                print(df[df.Status == "Finished"].to_csv(
                    sep='\t', index=False))

            elif filter == "All":
                print(df)

        except FileNotFoundError:
            print("No File Found")

    def delete_task(self, id):
        pass
