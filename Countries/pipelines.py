# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WeskyscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        field_names = adapter.field_names()
        floats = ['Area', 'population']
        try:
            for numbers in floats:
                value = adapter.get(numbers)
                adapter[numbers] = float(value)
            print('/////////////////////////////////////DONE!!!')

        except:
            print('Error................................../////')

        return item
