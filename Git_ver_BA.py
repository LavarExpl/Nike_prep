import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


class SalesData:
    def __init__(self, months, footwear_sales, apparel_sales):
        self.df = pd.DataFrame({'Month': months, 'Footwear Sales': footwear_sales, 'Apparel Sales': apparel_sales})

    def calculate_growth(self):
        self.df['Footwear Growth'] = self.df['Footwear Sales'].pct_change() * 100
        self.df['Apparel Growth'] = self.df['Apparel Sales'].pct_change() * 100

    def get_opportunity(self):
        footwear_opportunity = self.df['Footwear Growth'].max()
        apparel_opportunity = self.df['Apparel Growth'].max()
        return footwear_opportunity, apparel_opportunity


class SalesPlot:
    def __init__(self, sales_data):
        self.sales_data = sales_data

    def plot_sales(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.sales_data.df['Month'], self.sales_data.df['Footwear Sales'], marker='o', label='Footwear Sales')
        plt.plot(self.sales_data.df['Month'], self.sales_data.df['Apparel Sales'], marker='o', label='Apparel Sales')
        plt.title('Nike Basketball Sales Analysis (2022-2023)')
        plt.xlabel('Months')
        plt.ylabel('Sales')
        plt.legend()

    def show_opportunity_analysis(self):
        opportunity_analysis = self.sales_data.get_opportunity()
        text = f"\nOpportunity Analysis (2022-2023):\n\nFootwear Sales Growth Opportunity: {opportunity_analysis[0]:.2f}%\nApparel Sales Growth Opportunity: {opportunity_analysis[1]:.2f}%"
        plt.text(0.5, 0.1, text, transform=plt.gca().transAxes, fontsize=5, verticalalignment='center')
        plt.show()

    def save_to_csv(self, filename='sales_data.csv'):
        self.df.to_csv(filename, index=False)


def main():
    # Dummy data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    footwear_sales = [15000, 18000, 22000, 25000, 28000, 30000]
    apparel_sales = [8000, 10000, 12000, 15000, 18000, 20000]
    # Create instances of classes
    sales_data = SalesData(months, footwear_sales, apparel_sales)
    sales_data.calculate_growth()
    sales_plot = SalesPlot(sales_data)
    sales_plot.plot_sales()
    sales_plot.show_opportunity_analysis()



if __name__ == "__main__":
    main()

# Open the file using the default Excel application on Windows
try:
    os.system(f'start excel {"sales_data.csv"}')
except Exception as e:
    print(f'Error opening file: {e}')