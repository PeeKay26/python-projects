import pandas as pd
import matplotlib.pyplot as plt

# load the csv file into a pandas dataframe
databmi = pd.read_csv('BMI.csv', sep=",")

while True:
    print("""
    Choose an operation:
    1. Male Data
    2. Female Data
    3. Mean Height
    4. Mean Male Height
    5. Mean Female Height
    6. Mean Weight
    7. Mean Male Weight
    8. Mean Female Weight
    9. Count of Each Index Value
    10. Plot Male and Female Mean Height
    11. Plot Male and Female Mean Weight
    12. Plot Male and Female Mean Index
    13. Pie Chart of Index Values
    14. Description and Count of Index Values
    0. Exit
    """)
    choice = input('Enter your choice: ')

    if choice == '1':
        maleData = databmi[databmi['Gender'] == 'Male']
        print(maleData)

    elif choice == '2':
        femaleData = databmi[databmi['Gender'] == 'Female']
        print(femaleData)

    elif choice == '3':
        meanHeight = databmi['Height'].mean()
        print('Mean height:', meanHeight)

    elif choice == '4':
        meanHeightMale = databmi[databmi['Gender'] == 'Male']['Height'].mean()
        print('Mean male height:', meanHeightMale)

    elif choice == '5':
        meanHeightFemale = databmi[databmi['Gender'] == 'Female']['Height'].mean()
        print('Mean female height:', meanHeightFemale)

    elif choice == '6':
        meanWeight = databmi['Weight'].mean()
        print('Mean weight:', meanWeight)

    elif choice == '7':
        meanWeightMale = databmi[databmi['Gender'] == 'Male']['Weight'].mean()
        print('Mean male weight:', meanWeightMale)

    elif choice == '8':
        meanWeightFemale = databmi[databmi['Gender'] == 'Female']['Weight'].mean()
        print('Mean female weight:', meanWeightFemale)

    elif choice == '9':
        count = databmi['Index'].value_counts()
        print(count)

    elif choice == '10':
        mean_male_height = databmi[databmi['Gender'] == 'Male']['Height'].mean()
        mean_female_height = databmi[databmi['Gender'] == 'Female']['Height'].mean()
        plt.bar(['Male', 'Female'], [mean_male_height, mean_female_height])
        plt.title('Mean Male Height vs Mean Female Height')
        plt.xlabel('Gender')
        plt.ylabel('Mean Height')
        plt.show()

    elif choice == '11':
        mean_male_weight = databmi[databmi['Gender'] == 'Male']['Weight'].mean()
        mean_female_weight = databmi[databmi['Gender'] == 'Female']['Weight'].mean()
        plt.bar(['Male', 'Female'], [mean_male_weight, mean_female_weight])
        plt.title('Mean Male Weight vs Mean Female Weight')
        plt.xlabel('Gender')
        plt.ylabel('Mean Weight')
        plt.show()

    elif choice == '12':
        mean_male_index = databmi[databmi['Gender'] == 'Male']['Index'].mean()
        mean_female_index = databmi[databmi['Gender'] == 'Female']['Index'].mean()
        plt.bar(['Male', 'Female'], [mean_male_index, mean_female_index])
        plt.title('Mean Male Index vs Mean Female Index')
        plt.xlabel('Gender')
        plt.ylabel('Mean Index')
        plt.show()

    elif choice == "13":
        plt.pie(databmi['Index'].value_counts(), labels=['Extremely Weak', 'Weak', 'Normal','Overweight','Obesity','Extreme Obesity'],colors=['red','lightgreen','pink','gold','brown','skyblue'])
        plt.title("Index Distribution")
        plt.show()

    elif choice == '14':
        labels = ['Extremely Weak', 'Weak', 'Normal','Overweight','Obesity','Extreme Obesity']
        # for i in labels:
        #     print(f"{i}: {databmi['Index'].value_counts()}")
        for i in databmi['Index'].value_counts().index:
            if (i == 1):
                print(f"{labels[0]}: {databmi['Index'].value_counts()[i]}")
            elif (i == 2):
                print(f"{labels[1]}: {databmi['Index'].value_counts()[i]}")
            elif (i==3):
                print(f"{labels[2]}: {databmi['Index'].value_counts()[i]}")        
            elif(i == 4):
                print(f"{labels[3]}: {databmi['Index'].value_counts()[i]}")
            elif (i==5):
                print(f"{labels[4]}: {databmi['Index'].value_counts()[i]}")   
            else:
                print(f"{labels[5]}: {databmi['Index'].value_counts()[i]}")
        print (f"Total Sample Size: {databmi['Index'].value_counts().sum()}")

    elif choice == '15':
        maleHM = databmi[databmi['Gender'] == 'Male'].head(10)['Height']
        maleWM = databmi[databmi['Gender'] == 'Male'].head(10)['Weight']
        femaleHM = databmi[databmi['Gender'] == 'Female'].head(10)['Height']
        femaleWM = databmi[databmi['Gender'] == 'Female'].head(10)['Weight']
        plt.plot(maleHM,maleWM,marker="*",color="blue")
        plt.plot(femaleHM,femaleWM,marker="*",color="pink")
        plt.title('Height to Weight of Males vs Females')
        plt.xlabel("Height in cms")
        plt.ylabel("Weight in kgs")
        plt.show()

    elif choice == '0':
        break

    else:
        print('Invalid choice. Try again: ')