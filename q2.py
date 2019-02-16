'''
You are given a text file where each line contains a JSON message as string, containing three fields: sold_by_user_id (string), product_sold_id (string), and quantity (integer). You can assume that each line is a valid JSON message.

For instance, a text file may contain the following three lines:
{"sold_by_user_id" : "uid_1", "product_sold_id" : "pid_1", "quantity" : 45}
{"sold_by_user_id" : "uid_1", "product_sold_id" : "pid_2", "quantity" : 1}
{"sold_by_user_id" : "uid_2", "product_sold_id" : "pid_2", "quantity" : 5}

Given this as input (assume that it is a text file stored in your local machine), write a program that reads the file, and computes the most popular product_solds based on two ranking methods.

(1) Based on the unique number of sold_by_users who purchased each product_sold, and
(2) Based on the total quantity of each product_sold sold.

For instance, using the above example with 3 data points, the most popular product_sold based on ranking method #1 is "pid_2" because it was purchased by two different sold_by_users (where as "pid_1" was purchased only by one sold_by_user).
On the other hand, using ranking method #2, "pid_1" is the winner as 45 units of "pid_1" was sold whereas only 1+5=6 units of "pid_2" was sold.

In case of ties, your program must output the product_sold ids that are tied.
The output can be simply printed to the console in a human-readable manner.
Refer to the sample output message below.

Sample Output:
Most popular product_sold(s) based on the number of purchasers: [ "pid_2" ]
Most popular product_sold(s) based on the quantity of goods sold: [ "pid_1" ]
'''
import csv
from collections import Counter, defaultdict

class Solution:
    def __init__(self):
        self.sold_by_user = Counter()
        self.product_sold = Counter()
        self.unique_buyer = defaultdict(set)

    def process(self, filename):
        with open(filename, newline='') as file:
            buffer = csv.reader(file)
            for row in buffer:
                parsed = eval(row[0])
                uid = parsed['user_id']
                pid = parsed['product_id']
                psd = parsed['quantity']
                if uid not in self.unique_buyer[pid]:
                    self.sold_by_user[pid] += 1
                    self.unique_buyer[pid].add(uid)
                self.product_sold[pid] += psd

    def getRankByUniquePurchase(self):
        res = self.sold_by_user.most_common()
        max_sold = res[0][1]
        ret = []
        for pid, sold in res:
            if max_sold > sold:
                break
            ret.append(pid)
        return ret

    def getRankBySolds(self):
        res = self.product_sold.most_common()
        max_sold = res[0][1]
        ret = []
        for pid, sold in res:
            if max_sold > sold:
                break
            ret.append(pid)
        return ret

    def printRank(self):
        print('''
        Most popular product_sold(s) based on the number of purchasers: [{0}]
        Most popular product_sold(s) based on the quantity of goods sold: [{1}]
        '''.format(self.getRankByUniquePurchase(), self.getRankBySolds()))
