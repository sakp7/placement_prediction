import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df= pd.read_csv("collegePlace.csv")

le=LabelEncoder()
stream=le.fit_transform(df['Stream'])
df["Stream"]=stream
x=df.pop("Stream")
df.insert(2,"Stream",x)


x=le.fit_transform(df["Gender"])
df.drop("Gender",axis=1,inplace=True)
df.insert(1,"Gender",x)



x_train,x_test,y_train,y_test=train_test_split(df[['Age','Gender','Stream','Internships','CGPA','HistoryOfBacklogs']],df.PlacedOrNot,test_size=0.2)
model=LogisticRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

def fun():
    
    age=st.number_input("Enter Age")
    gender=st.radio("Gender",("Male","Female"))
    if gender=="male":
        gender=1
    else:
        gender=0
    
    
    st1=st.radio("Select Stream:",("ECE","CS","IT","MECH","CIVIL"))
    if(st1=="ECE"):
        st1=3
    elif st1=="CS":
        st1=1
    elif st1=="IT":
        st1=4
    elif st1=="MECH":
        st1=5
    else:
        st1=2
    
    
    intern=st.radio("InterShip Done ?",("Yes","No"))
    if intern=="Yes":
        intern=1
    else:
        intern=0
    
    gpa=st.number_input("Enter CGPA")
    
    back=st.number_input("History of Backlogs")
    li=[age,gender,st1,intern,gpa,back]
    #print(li)
    predict=model.predict([li])
    if st.button("Submit"):
        if predict==1:
            st.success("Congratulations you got the placement")
        else:
            st.error("Sorry you did not get the placement")
    
        
fun()
