import pandas as pd
import os
import time

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
            "Status": "Not Assigned",
            "Description": short_description
        }

        df = pd.concat([self.df, pd.DataFrame(
            [created_data])], ignore_index=True)

        if os.path.exists(self.output_path):
            df.to_csv(self.output_path, mode='a', header=False, index=False)
            
        else:
            df.to_csv(self.output_path, mode='w', header=True, index=False)
        print("Successfuly created a new task")
        time.sleep(2)

    def show_tasks(self, filter):
        try:
            df = pd.read_csv("output.csv", sep=",")
            if filter == "New":
                print(df[df.Status == "New"])

            elif filter == "In Progress":
                print(df[df.Status == "In Progress"])

            elif filter == "Finished":
                print(df[df.Status == "Finished"])

            elif filter == "All":
                print(df)

        except FileNotFoundError:
            print("No File Found")

    def edit_task(self, id, position, text):
        try :
            df = pd.read_csv("output.csv", sep=",")
            if position.lower() == "name":
                df.loc[[int(id)], "Name"] = text
                df.to_csv(self.output_path,mode="w", header=True, index=False)
                print("Successfuly edited task")
                time.sleep(2)
            elif position.lower() == "description":
                df.loc[[int(id)], "Description"] = text
                df.to_csv(self.output_path,mode="w", header=True, index=False)
                print("Successfuly edited task")
                time.sleep(2)
            elif position.lower() == "status":
                s = {"1" : "Not Assigned", "2" : "In Progress", "3" : "Finished"}
                df.loc[[int(id)], "Status"] = s[text]
                df.to_csv(self.output_path,mode="w", header=True, index=False)
                print("Successfuly changed status")
                time.sleep(2)
            else : 
                "Not a valid parameter. Try Again"
        except ValueError:
            "ID not found. Try Again"


    def delete_task(self, id):
        df = pd.read_csv("output.csv", sep=",")
        if input("Are you sure you want to delete this line ?").lower() == "yes":
            df.drop(int(id), axis=0, inplace=True)
            df.to_csv(self.output_path,mode="w", header=True, index=False)
            print("Successfuly deleted task")
            time.sleep(2)
            
