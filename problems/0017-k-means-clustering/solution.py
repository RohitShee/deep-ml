def calculate_distance(point1 : tuple[float, ...], point2 : tuple[float, ...]) -> float :
	distance = 0.0
	for x1, x2 in zip(point1,point2) :
		distance+= (x1-x2)**2
	return distance


def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	# Your code here
	centroids = initial_centroids
	for _ in range(max_iterations) :
		point_clusters =[[] for i in range(k)]
		for point in points :
			distances = [calculate_distance(point,centroid) for centroid in centroids]
			index , min_dist = min(enumerate(distances), key = lambda x : x[1])
			point_clusters[index].append(point)
		centroids = [tuple(sum(col)/len(col) for col in zip(*cluster_points)) for cluster_points in point_clusters]	

	return centroids