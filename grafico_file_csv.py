import csv
import matplotlib.pyplot as plt

def dict_whit_data(clave, value):
    iterable = zip(clave, value)
    country_dict = {k:v for k, v in iterable if 'Country' in k or 'Population' in k}
    return country_dict

def read_csv():
    with open('../intermedio/archivos/world_population.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = list(map(lambda value: dict_whit_data(header, value) ,reader))
        return data
   
def generate_bar_chart(data, country):
    result = list(filter(lambda item : item['Country/Territory'] == country, data))[0]
    labels = list(result.keys())[1:9]
    values = list(map(int,list(result.values())[1:9]))
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


def run():
    data = read_csv()
    generate_bar_chart(data, 'Peru')


if __name__ == '__main__':
    run()
