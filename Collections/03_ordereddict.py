# -*- coding: utf-8 -*-
# 
# (c) @paskwal, 2019

# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

# Task
# You are the manager of a supermarket. 
# You have a list of N items together with their prices that consumers bought on a particular day. 
# Your task is to print each item_name and net_price in order of its first occurrence.
#       item_name = Name of the item. 
#       net_price = Quantity of the item sold multiplied by the price of each item.

# Input Format
# The first line contains the number of items, N. 
# The next N lines contains the item's name and price, separated by a space.

# Output Format
# Print the item_name and net_price in order of its first occurrence.


from collections import OrderedDict

items_bought = OrderedDict()


if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        data = input().split()
        net_price = float(data.pop())
        item_name = " ".join(data)

        if item_name in items_bought:
            items_bought[item_name] += net_price
        else:
            items_bought[item_name] = net_price
        
    # print(items_bought)
    for item in items_bought:
        print(item, "%.0f" % items_bought[item])

