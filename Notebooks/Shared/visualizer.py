import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Visualizer:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.df = dataframe

    def update_df(self, df: pd.DataFrame) -> None:
        self.df = df

    def make_histogram(self, variable: str, binwidth: int, lower_limit: int = None, upper_limit: int = None) -> None:
        if upper_limit is None:
            upper_limit = self.df[variable].max()
        if lower_limit is None:
            lower_limit = self.df[variable].min()
        bins = np.arange(lower_limit, upper_limit + binwidth, binwidth)
        plt.hist(self.df[variable], bins=bins, edgecolor='black',
                 alpha=0.75, range=[self.df[variable].min(), upper_limit])
        plt.ylabel("antall")
        plt.xlabel(variable)

    def make_scatter_plot(self, para1: str, para2: str, logx: bool = False, logy: bool = False):
        plt.plot(self.df[para1], self.df[para2], '*', alpha=0.1)
        if logx:
            plt.xscale("log")
        if logy:
            plt.yscale('log')
        plt.xlabel(para1)
        plt.ylabel(para2)

    def corr_heatmap(self, figsize=(10, 10)):
        _, axs = plt.subplots(figsize=figsize)
        ax = sns.heatmap(
            self.df.corr(), vmin=-1, vmax=1, cmap="BrBG", linewidths=0.5, annot=True, ax=axs)
        ax.set_title('Correlation matrix')
        return ax
