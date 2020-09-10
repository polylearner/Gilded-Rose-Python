class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_half_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 11:
                    self.increase_quality(item)
                if item.sell_in < 6:
                    self.increase_quality(item)

    def decrease_quality(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.quality = item.quality - 1     

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    self.decrease_quality(item)
            else:
                self.update_half_quality(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.quality > 0:
                                self.decrease_quality(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    self.increase_quality(item)
