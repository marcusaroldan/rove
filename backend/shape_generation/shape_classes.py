
class Point():

    def __init__(self, 
                lon,
                lat,
                type,
                radius,
                rank_candidates='true',
                preferred_side='same',
                node_snap_tolerance=0,
                street_side_tolerance=0):
        
        self.point_parameters = {
            {'lon': lon,
            'lat': lat,
            'type': type,
            'radius': radius,
            'rank_candidates': rank_candidates,
            'preferred_side': preferred_side,
            'node_snap_tolerance': node_snap_tolerance,
            'street_side_tolerance':street_side_tolerance
            }
        }

class Vahalla_Request():
    turn_penalty_factor = 100000 # Penalizes turns in Valhalla routes. Range 0 - 100,000.
    stop_radius = 35 # Radius used to search when matching stop coordinates (meters)
    intermediate_radius = 100 # Radius used to search when matching intermediate coordinates (meters)
    
    stop_distance_threshold  = 1000 # Stop-to-stop distance threshold for including intermediate coordinates (meters)
    maneuver_penalty = 43200 # Penalty when a route includes a change from one road to another (seconds). Range 0 - 43,200. 
    
    default_filters = {
                        'attributes': ['edge.id', 'edge.length', 'shape'],
                        'action':'include'
                        }
    default_costing_options = {
                        'bus':{
                            'maneuver_penalty': maneuver_penalty
                            }
                        }
    def __init__(self,
                shape=None,
                costing='bus',
                shape_match='map_snap',
                fiters=default_filters,
                costing_options=default_costing_options,
                trace_options_turn_penalty_factor=turn_penalty_factor):

        self.request_parameters = {'shape': shape,
                'costing': costing,
                'shape_match': shape_match,
                'filters': fiters,
                'costing_options': costing_options,
                'trace_options.turn_penalty_factor':trace_options_turn_penalty_factor 
                }

class Pattern: # Attributes for each unique pattern of stops that create one or more route variant
    def __init__(self, route, direction, stops, trips, stop_coords, shape, timepoints):
        self.route = route
        self.direction = direction
        self.stops = stops
        self.trips = trips
        self.stop_coords = stop_coords
        self.shape = shape
        self.timepoints = timepoints
        self.shape_coords = 0
        self.v_input = 0
        self.coord_types = 0
        self.radii = 0

class Segment: # Attributes for each segment which make up a pattern
    def __init__(self, geometry, distance):
        self.geometry = geometry
        self.distance = distance
            
class Corridor: # Attributes for each corridor
    def __init__(self, edges, segments):
        self.edges = edges
        self.segments = segments
        self.passenger_shared = []
        self.stop_shared = []
        
    def get_edges(self):
        return self.edges
    
    def get_segments(self):
        return self.segments
    
    def get_pass_shared(self):
        return self.passenger_shared
    
    def get_stop_shared(self):
        return self.stop_shared