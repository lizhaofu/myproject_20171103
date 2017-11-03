from sklearn import metrics
labels_true = [0, 0, 0, 1, 1, 1]
labels_pred = [0, 0, 1, 1, 2, 2]

print(metrics.homogeneity_score(labels_true, labels_pred))

print(metrics.completeness_score(labels_true, labels_pred))

print(metrics.v_measure_score(labels_true, labels_pred))
