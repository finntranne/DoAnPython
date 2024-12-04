import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("NewMales.csv")

def Wage_Edu(df, year=None, ax=None):
    """
    Bieu do Wage vs Education: Giup phan tich moi quan he giua muc luong (Wage) 
    va so nam hoc tap (Education) cua nguoi lao dong.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    if year is not None:
        df = df[df['year'] == year]
    sns.scatterplot(x='school', y='wage', data=df, ax=ax)
    ax.set_title(f'Wage vs Education (Years of Schooling) - Year {year}' if year else 'Wage vs Education (Years of Schooling)')
    ax.set_xlabel('Years of Schooling')
    ax.set_ylabel('Wage')
    ax.grid(True)
    if ax is None:
        plt.show()

def Wage_Ind(df, year=None, ax=None):
    """
    Bieu do Wage by Industry: Phan tich su khac biet ve muc luong (Wage) 
    giua cac nganh nghe (Industry) khac nhau.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 8))
    if year is not None:
        df = df[df['year'] == year]
    sns.boxplot(x='industry', y='wage', data=df, color='lightblue', ax=ax)
    ax.set_title(f'Wage by Industry - Year {year}' if year else 'Wage by Industry')
    ax.set_xlabel('Industry')
    ax.set_ylabel('Wage')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True)
    if ax is None:
        plt.show()

def Wage(df, year = None ,ax=None):
    """
    Bieu do Wage Distribution: Phan tich phan phoi muc luong (Wage) trong toan bo du lieu.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    if year is not None:
        df = df[df['year'] == year]
    sns.histplot(df['wage'], kde=True, bins=30, ax=ax)
    ax.set_title('Distribution of Wage')
    ax.set_xlabel('Wage')
    ax.set_ylabel('Count')
    if ax is None:
        plt.show()

def plot_ethn(df, year=None, ax=None):
    """
    Bieu do Ethnicity: Thong ke so luong nguoi lao dong thuoc cac nhom sac toc (Ethnicity).
    Hien thi bieu do tron.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    if year is not None:
        df = df[df['year'] == year]
    ethn_counts = df['ethn'].value_counts()
    ax.pie(
        ethn_counts, 
        labels=ethn_counts.index, 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=plt.cm.Paired.colors,
        textprops={'fontsize': 18}
    )
    ax.set_title(f'Ethnicity Distribution - Year {year}' if year else 'Ethnicity Distribution', fontsize=18)
    if ax is None:
        plt.tight_layout()
        plt.show()


def plot_maried(df, year=None, ax=None):
    """
    Bieu do Marital Status: Thong ke so luong nguoi lao dong theo tinh trang hon nhan (Marital Status).
    Hien thi bieu do tron.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))

    # Lọc dữ liệu theo năm nếu được cung cấp
    if year is not None:
        df = df[df['year'] == year]
    maried_counts = df['maried'].value_counts()
    ax.pie(
        maried_counts, 
        labels=maried_counts.index, 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=plt.cm.Paired.colors, 
        textprops={'fontsize': 18}
    )  
    ax.set_title(f'Marital Status Distribution - Year {year}' if year else 'Marital Status Distribution', fontsize=18)
    if ax is None:
        plt.tight_layout()
        plt.show()


def plot_health(df, year=None, ax=None):
    """
    Bieu do Health Status: Thong ke so luong nguoi lao dong theo tinh trang suc khoe (Health Status).
    Hien thi bieu do tron.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    if year is not None:
        df = df[df['year'] == year]  
    health_counts = df['health'].value_counts()
    ax.pie(
        health_counts, 
        labels=health_counts.index, 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=plt.cm.Paired.colors,
        textprops={'fontsize': 18}
    )   
    ax.set_title(f'Health Status Distribution - Year {year}' if year else 'Health Status Distribution', fontsize=18)
    if ax is None:
        plt.tight_layout()
        plt.show()


def plot_industry(df, year=None, ax=None):
    """
    Bieu do Industry: Thong ke so luong nguoi lao dong theo cac nganh nghe (Industry).
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 4))
    if year is not None:
        df = df[df['year'] == year]
    sns.countplot(y='industry', data=df, order=df['industry'].value_counts().index, ax=ax)
    ax.set_title(f'Count of Industry - Year {year}' if year else 'Count of Industry')
    ax.set_xlabel('Count')
    ax.set_ylabel('Industry')
    if ax is None:
        plt.tight_layout()
        plt.show()

def plot_occupation(df, year=None, ax=None):
    """
    Bieu do Occupation: Thong ke so luong nguoi lao dong theo cac nghe nghiep (Occupation).
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
    if year is not None:
        df = df[df['year'] == year]
    sns.countplot(y='occupation', data=df, order=df['occupation'].value_counts().index, ax=ax)
    ax.set_title(f'Count of Occupation - Year {year}' if year else 'Count of Occupation')
    ax.set_xlabel('Count')
    ax.set_ylabel('Occupation')
    if ax is None:
        plt.tight_layout()
        plt.show()

def plot_residence(df, year=None, ax=None):
    """
    Bieu do Residence: Thong ke so luong nguoi lao dong theo noi cu tru (Residence).
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
    if year is not None:
        df = df[df['year'] == year]
    sns.countplot(y='residence', data=df, order=df['residence'].value_counts().index, ax=ax)
    ax.set_title(f'Count of Residence - Year {year}' if year else 'Count of Residence')
    ax.set_xlabel('Count')
    ax.set_ylabel('Residence')
    if ax is None:
        plt.tight_layout()
        plt.show()
