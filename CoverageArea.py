class SENSOR:
    def __init__(self, location):
        self.x = location[0]
        self.y = location[1]

def mark_points(sensor, r, points, sensors_coverage):
    left, right, down, up = sensor.x - r, sensor.x + r, sensor.y - r, sensor.y + r
    sensor_coverage_count = 0
    r2 = r ** 2
    for i in range(max(left, 0), min(right, 1080)):
        for j in range(max(down, 0), min(up, 720)):
            if (sensor.x - i) ** 2 + (sensor.y - j) ** 2 <= r2:
                if not points[i][j]:
                    points[i][j] = True
                    sensor_coverage_count += 1
    sensors_coverage.append(sensor_coverage_count)
    return points, sensors_coverage

def convert_from_binlist_to_int(bin_list):
    return sum(j * (2 ** i) for i, j in enumerate(reversed(bin_list)))

def convert_to_SENSOR(locations, n_bits):
    bits_no_for_axis = (n_bits + 1) // 2
    sensors = []
    for location in locations:
        x_axis, y_axis = location[:bits_no_for_axis], location[bits_no_for_axis:]
        # convert from bin to dec
        x_axis = convert_from_binlist_to_int(x_axis)
        y_axis = convert_from_binlist_to_int(y_axis)
        sensors.append(SENSOR((x_axis, y_axis)))
    return sensors

def calculate(sensors_locations, n_bits, CRPS):
    # CRPS for 'Coverage Radius Per Sensor' 
    sensors = convert_to_SENSOR(sensors_locations, n_bits)
    points = [[False for _ in range(720)] for _ in range(1080)]
    sensors_coverage = []
    for sensor in sensors:
        points, sensors_coverage = mark_points(sensor, CRPS, points, sensors_coverage)
    total_covered_area = sum(sensors_coverage)
    return [total_covered_area, sensors_coverage]