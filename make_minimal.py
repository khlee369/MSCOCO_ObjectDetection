import json

with open('instances_val2017.json') as f:
    a = json.load(f)

d = dict([])
d['images'] = a['images']
d['annotations'] = a['annotations']
d['categories'] = a['categories']

for images_dict in d['images']:
    del images_dict['license']
    del images_dict['coco_url']
    del images_dict['date_captured']
    del images_dict['flickr_url']

for annotations_dict in d['annotations']:
    del annotations_dict['segmentation']
    # del annotations_dict['iscrowd']

for categories_dict in d['categories']:
    del categories_dict['supercategory']
    del categories_dict['name']

with open('minimal_2017.json', 'w') as json_file:
    json.dump(d, json_file)