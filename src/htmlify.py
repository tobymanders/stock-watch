from itertools import groupby
from operator import itemgetter
import sys

example = [(1575484924.4801579, '281', 'Richfield', '1000 West 78th St', 'Richfield', 'MN', '55423', 'airpods', 6084400.0), (1575484924.4801579, '8', 'Burnsville', '14141 Aldrich Ave S', 'Burnsville', 'MN', '55337', 'airpods', 6084400.0), (1575484924.4801579, '4', 'Minnetonka', '13513 Ridgedale Dr', 'Hopkins', 'MN', '55305', 'airpods', 6084400.0), (1575484924.4801579, '7', 'Roseville', '1643 County Road B2', 'Roseville', 'MN', '55113', 'airpods', 6084400.0), (1575484924.4801579, '10', 'Maplewood', '1795 County Rd D E', 'Maplewood', 'MN', '55109', 'airpods', 6084400.0), (1575484924.4801579, '11', 'Northtown', '300 Northtown Dr NE', 'Blaine', 'MN', '55434', 'airpods', 6084400.0), (1575484924.4801579, '15', 'Oakdale', '8301 3rd St N', 'Oakdale', 'MN', '55128', 'airpods', 6084400.0), (1575484924.4801579, '14', 'Rochester', '4050 Hwy 52 N', 'Rochester', 'MN', '55901', 'airpods', 6084400.0), (1575484924.4801579, '40', 'Eau Claire', '4090 Commonwealth Ave', 'Eau Claire', 'WI', '54701', 'airpods', 6084400.0), (1575484924.4801579, '18', 'La Crosse', '9420 State Road 16', 'Onalaska', 'WI', '54650', 'airpods', 6084400.0), (1575484924.4801579, '43', 'Duluth', '5105 Burning Tree Rd', 'Duluth', 'MN', '55811', 'airpods', 6084400.0), (1575484924.4801579, '17', 'Sioux Falls', '2101 W 41st St', 'Sioux Falls', 'SD', '57105', 'airpods', 6084400.0), (1575484924.4801579, '812', 'Ames', '1220 S Duff Ave', 'Ames', 'IA', '50010', 'airpods', 6084400.0), (1575484925.3037, '162', 'Parma', '7400 Brookpark Rd', 'Cleveland', 'OH', '44129', 'airpods', 6084400.0), (1575484925.3037, '279', 'North Olmsted', '5140 Great Northern Plz S', 'North Olmsted', 'OH', '44070', 'airpods', 6084400.0), (1575484925.3037, '285', 'Akron', '96 Rothrock Rd', 'Akron', 'OH', '44321', 'airpods', 6084400.0), (1575484925.3037, '286', 'North Canton', '6595 Strip Ave NW', 'North Canton', 'OH', '44720', 'airpods', 6084400.0), (1575484925.3037, '407', 'Gratiot', '30701 Gratiot Ave', 'Roseville', 'MI', '48066', 'airpods', 6084400.0), (1575484925.3037, '1406', 'Allen Park', '3349 Fairlane Dr', 'Allen Park', 'MI', '48101', 'airpods', 6084400.0), (1575484925.3037, '1095', 'Chesterfield', '50400 Waterside Dr', 'Chesterfield', 'MI', '48051', 'airpods', 6084400.0), (1575484925.3037, '585', 'North Hills', '4801 McKnight Rd', 'Pittsburgh', 'PA', '15237', 'airpods', 6084400.0)]



def htmlify(list_of_tuples):
	
	for name, rows in groupby(results, itemgetter(0)):
	     table = []
	     for value0, value1, value2, value3, value4, value5, value6, value7, value8 in rows:
	        table.append(
	            "<tr><td>{}</td><td>{}</td><td>{}<td><td>{}</td><td>{}</td><td>{}<td><td>{}</td><td>{}</td><td>{}</td><td></tr>".format(
	                value0, value1, value2, value3, value4, value5, value6, value7, value8))

	return table

if __name__ == "__main__":
	if len(sys.argv)>1:
		results = sys.argv[1]
	else:
		results = example
	htmlify(results)