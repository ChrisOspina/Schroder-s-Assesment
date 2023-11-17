import pandas as pd
import pandas as pd                 # For data manipulation and analysis
import matplotlib.pyplot as plt     # Plotting library for Python programming language and it's numerical mathematics extension NumPy
import seaborn as sns               # Provides a high level interface for drawing attractive and informative statistical graphics

class Methods:
       
        #this method converts the AUM from a string to a numeric
        #@param dataset: the raw dataset
        def AUM_to_numeric(dataset):
                dataset['AUM'] = pd.to_numeric(dataset['AUM'].str.replace(',', '').str.replace('$', ''), errors='coerce')
                return dataset
        
        #this method converts the NetFlows from a string to a numeric
        #@param dataset: the raw dataset
        def NetFlows_to_numeric(dataset):
                dataset['NetFlow'] = pd.to_numeric(pd.to_numeric(dataset['NetFlow'].str.replace(',', '').str.replace('$', ''), errors='coerce'))
                return dataset


        #This method creates a pivot table by taking that charts 
        # the calendar quarter growth in AUM by both Asset Class and Client Group.
        #@param1 dataset: the raw dataset 
        #@param2 country: the filter country (United States, Canada or Mexico)
        def asset_class_pivot(dataset, country):
                filtered_dataset = dataset[dataset['Client Country'] == '${country}']
                pivot_table = pd.pivot_table(dataset, values='AUM', index=['Asset Class', 'Client Group'], columns='Quarter/Year (Asset Date)', aggfunc='sum')
                return pivot_table


        #this method creates a line graph based on the pivot table created from the above method
        #@param pivot_table: the pivot table created via the method above
        def line_graph_asset_class(pivot_table):
                pivot_table.plot(kind='line', marker='o', figsize=(12, 6))
                plt.title('Quarterly AUM Growth by Asset Class and Client Group')
                plt.xlabel('Asset Class, Client Group')
                plt.ylabel('AUM')
                plt.legend(title='Quarter-Year', loc='upper right')
                plt.grid(True)
                plt.show()

                return 
        

        #This method creates a pivot table that shows the cumulative NetFlows
        # going into the different Product Display Lens. There are filters for: (1) Client Group; (2) Channel; and Fund Strategy.
        #@param dataset: the raw dataset
        def net_flow_pivot(dataset):
               pivot_table = pd.pivot_table(dataset,values='NetFlow',
                index=['Product Display Lens'],columns=['Client Group', 'Channel', 'Fund Strategy'],aggfunc='cumsum',fill_value=0)
               return pivot_table
        

        #this method creates a line graph based on the pivot table created from the above method
        #@param pivot_table: the pivot table created via the method above
        def line_graph_net_flow(pivot_table):
                pivot_table.plot(kind='line', figsize=(12, 6))
                plt.title('Cumulative NetFlows by Product Display Lens')
                plt.xlabel('Product Display Lens')
                plt.ylabel('Cumulative NetFlow')
                plt.legend(title=('Client Group', 'Channel', 'Fund Strategy'), loc='upper left', bbox_to_anchor=(1, 1))
                plt.grid(True)
                plt.show()

                return
        
        #this method creates a pivot table to prep for a heatmap that can easily identify 
        #the Channel with the largest latest AUM (6/30/2023) by the Product Display Lens. There is a filter for the Fund Strategy.
        #@param1 dataset: the raw dataset
        #@param2 strategy: the fund strategy to filter the data by
        def heatmap_pivot(dataset, strategy):
                latest_data = dataset[dataset['Quarter/Year (Asset Date)'] == '4/1/2023']
                latest_data_filtered = latest_data[latest_data['Fund Strategy'] == '${strategy}']

                heatmap_pivot = pd.pivot_table(
                        latest_data_filtered,
                        values='AUM',
                        index='Product Display Lens',
                        columns='Channel',
                        aggfunc='max',
                        fill_value=0
                )
                return heatmap_pivot
        
        #this method creates the heatmap
        #@param heatmap_pivot: the pivot table created via the method above
        def create_heatmap(heatmap_pivot):
                plt.figure(figsize=(12, 8))
                sns.heatmap(heatmap_pivot, annot=True, fmt=".2f", cmap="YlGnBu", cbar_kws={'label': 'AUM'})
                plt.title('Channel with the Largest Latest AUM by Product Display Lens (Filtered by Fund Strategy)')
                plt.show()

                return
        