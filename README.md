# 3D_map_visualizer
A small project to visualize selected parts or regions on map in 3D map similar to google earth.

## Technologies used:

Django 2.x, Babylonjs, Google Maps Api, Mapbox static Api.

## Implementation:

Select the center of region to be selected by clicking on an embedded google map.(You can customize the scope of region by tweaking with the zoom parameter)
After selecting appropriate number of regions click on visualize.
You will see a 3D figure (pentagonal prism by default which can be changed by tweaking babylon part. Use an icosphere for google earth like experience).
This figure will have each of the selected regions on its faces.
