county_data = read.csv("/Users/sambarbeau/Documents/UIUC/DSC/web/data/county_data_PCA.csv")

## find correlation matrix
county_data_corr <- county_data[, -c(1:4,93)]
cor_matrix <- cor(county_data_corr, use = "complete.obs")
indices <- which(abs(cor_matrix) > 0.3, arr.ind = TRUE)

## Extract variable names with correlations and their corresponding values
high_correlation_variables <- data.frame(
  variable1 = rownames(cor_matrix)[indices[, 1]],
  variable2 = colnames(cor_matrix)[indices[, 2]],
  correlation_value = cor_matrix[indices]
)