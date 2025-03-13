#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# In[2]:


df = pd.read_csv("/Users/Nika/Downloads/SIS_Faculty-List.csv",encoding ="Latin")


# In[3]:


df[df.duplicated()]


# In[4]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap="viridis")


# In[5]:


print(df[df["LWD"].notnull()])


# In[104]:


print(df.columns)


# In[6]:


total_rows = df.shape[0]  # Or you can use len(df)

print(f'Total data points in the file: {total_rows}')


# In[105]:


# LWD is fiiled with future date for tagging unknown data
df["LWD"] = df["LWD"].fillna("20-Oct-2100")


# In[106]:


df.isnull().sum()


# In[107]:


df.info()


# In[108]:


uni_list = df[df["Location"].isnull()]["University"]

uni_locations = df[df["University"].isin(uni_list)]

print(uni_locations[["University", "Location"]])


# In[109]:


# Assign Universities with Location
university_to_location = {
    "University of Westminster": "Westminster",
    "University Of Johannesburg": "Johannesburg",
    "University of Toronto": "Toronto",
    "The University of Hull": "Liverpool",
    "Michigan State University, USA": "Michigan",
    "University of Nebraska,USA": "Cardiff",
    "Girne American University, Cyprus": "Girne",
    "National University of Singapore": "Singapore",
    "Nova Southeastern University, USA": "Fort Lauderdale",
    "International Islamic University  Malaysia": "Malaysia",
    "University of Salento, Italy": "Salento",
    "PaulCezannel University, France": "Aix-en-Provence",
    "University of Paris 1 Pantheon-Sorbonne France": "Paris",
    "Colorada State University, USA": "Colorada",
    "International Islamic University< Malaysia": "Malaysia"
}




# In[110]:


#Apply locations to empty location columns in which University is avaulable
df["Location"] = df.apply(lambda row: university_to_location.get(row["University"], row["Location"]), axis=1)


# In[112]:


df.isnull().sum()


# In[113]:


df["ID"] = df["ID"].fillna(lambda x: np.random.randit(1,1000))

#fILL Missing values with random numbers


# In[114]:


df.isnull().sum()


# In[20]:


df[["Courses Taught- Term 201510","University"]]


# In[21]:


df[df["Location"] == "Cambridge"][["University"]]


# In[116]:


df[df["University"].isnull()][["Courses Taught- Term 201510","University"]]


# In[117]:


df.loc[df["Name"] == "Ludmilla Sirnov", ["Highest\nQualification\nLevel", "Highest Qualification", "Major","University"]] = df.loc[df["Name"] == "Ludmilla Sirnov", ["Highest\nQualification\nLevel", "Highest Qualification", "Major","University"]].fillna({"Highest\nQualification\nLevel": "Masters", "Highest Qualification": "Masters", "Major": "Business Management","University":"Swiss Management Center"})


# In[118]:


df["Join\nDate"] = df["Join\nDate"].fillna("20.05.2050") # Future Value for tagging as unknown data


# In[119]:


df["Reports To"] = df["Reports To"].fillna(df["Reports To"].mode()[0])  # Most frequent value


# In[120]:


df["Major"] = df["Major"].fillna(df["Major"].mode()[0])  # Most frequent value


# In[121]:


df["MAJOR TEACHING FIELD"] = df["MAJOR TEACHING FIELD"].fillna(df["MAJOR TEACHING FIELD"].mode()[0])  # Most frequent value


# In[122]:


df["DOCUMENT OTHER PROFESSIONAL CERTIFICATION CRITIERA Five Years Work Experience Teaching Excellence Professional Certifications"] = df["DOCUMENT OTHER PROFESSIONAL CERTIFICATION CRITIERA Five Years Work Experience Teaching Excellence Professional Certifications"].fillna(df["DOCUMENT OTHER PROFESSIONAL CERTIFICATION CRITIERA Five Years Work Experience Teaching Excellence Professional Certifications"].mode()[0])  # Most frequent value


# In[123]:


df["All Qualifications from Profile"] = df["All Qualifications from Profile"].fillna(df["All Qualifications from Profile"].mode()[0])  # Most frequent value


# In[124]:


df["Highest\nQualification\nLevel"] = df["Highest\nQualification\nLevel"].fillna(df["Highest\nQualification\nLevel"].mode()[0])  # Most frequent value


# In[125]:


df["Courses Taught- Term 201510"] = df["Courses Taught- Term 201510"].fillna(df["Courses Taught- Term 201510"].mode()[0])  # Most frequent value


# In[126]:


df["University"] = df["University"].fillna(df["University"].mode()[0])  # Most frequent value


# In[127]:


df["Location"] = df["Location"].fillna(df["Location"].mode()[0])  # Most frequent value


# In[129]:


df["Highest Qualification"] = df["Highest Qualification"].fillna(df["Highest Qualification"].mode()[0])


# In[130]:


df.isnull().sum()


# In[ ]:




