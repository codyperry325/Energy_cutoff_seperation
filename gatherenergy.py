import pandas as pd
import os 

def energy_range(df,energy_diff):
    names=[]
    energies = df["energy"]
    globalmin = min(energies)
    with open("bottom_30.txt","w+") as bot:
        bot.write(f"File names that are below {energy_diff} \n")
    for item in energies:
        ediff = item - globalmin
        if ediff <= energy_diff:
            ind = df.index[df['energy'] == item].tolist()[0]
            name = df.at[ind,'id']
            names.append(name)
            with open("bottom_30.txt", "a+") as bot:
                bot.write(f"{name} \n")
    return names

def copy_files(names):
    for name in names:
        filename = f"{name}.cif"
        try:
            os.mkdir("Energy_cutoff")
        except FileExistsError:
            pass
        if os.path.exists(filename):
            os.rename(filename,f"Energy_cutoff/{filename}")
        else:
            print("File Does Not Exist")
            continue  
        
def main():
    energy_diff = 15
    df = pd.read_csv("structures.csv")
    names = energy_range(df,energy_diff)
    copy_files(names)

if __name__ == "__main__":
    main()
