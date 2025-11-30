from Instructions.Machine_Learning.Supervised.Classification.decision_tree import decision_tree_explanation
from Instructions.Machine_Learning.Supervised.Classification.logistic_regression import logistic_regression_explanation
from Instructions.Machine_Learning.Supervised.Classification.random_forest import random_forest_explaination
from Instructions.Machine_Learning.Supervised.Classification.svm import svm_explanation
from Instructions.Machine_Learning.Supervised.Classification.knn import knn_explanation
from Instructions.Machine_Learning.Supervised.Classification.nb import naive_bayes_explanation
from Instructions.Machine_Learning.Supervised.Regression.linear_regression import linear_regression_markdown
from Instructions.Machine_Learning.Supervised.Regression.ridge_r import ridge_regression_markdown
from Instructions.Machine_Learning.Supervised.Regression.lasso_r import lasso_markdown_code
from Instructions.Machine_Learning.Supervised.Regression.elasticnet import elastic_net_markdown
from Instructions.Machine_Learning.Unsupervised.Clustering.kmeans import kmeans_explanation
from Instructions.Machine_Learning.Unsupervised.Clustering.hierarchial_clustering import hierarchial_markdown_code
from Instructions.Machine_Learning.Unsupervised.Clustering.dbscan import dbscan_markdown
from Instructions.Machine_Learning.Unsupervised.Clustering.gmm import gmm_explanation
from Instructions.Machine_Learning.Unsupervised.Dimensionality_Reduction.pca import pca_markdown_code
from Instructions.Machine_Learning.Unsupervised.Dimensionality_Reduction.svd import svd_markdown_code
from Instructions.Machine_Learning.Unsupervised.Dimensionality_Reduction.lda import lda_markdown_code
from Instructions.Machine_Learning.Unsupervised.Anomaly_Detection.z_score import zscore_markdown

SML_CLS_MAPPER = {
    "Logistic Regression": [
        logistic_regression_explanation,
        "./Instructions/Machine_Learning/Supervised/Classification/sigmoid.png",
        "https://www.youtube.com/results?search_query=logistic+regression+machine+learning"
    ],
    "Decision Tree": [
        decision_tree_explanation,
        "./Instructions/Machine_Learning/Supervised/Classification/dt.jpeg",
        "https://www.youtube.com/results?search_query=decision+tree+machine+learning+"
    ],
    "Random Forest": [
        random_forest_explaination,
        "./Instructions/Machine_Learning/Supervised/Classification/random_forest.png",
        "https://www.youtube.com/results?search_query=random+forest++machine+learning+"
    ],
    "Support Vector Machine": [
        svm_explanation,
        "./Instructions/Machine_Learning/Supervised/Classification/svm.png",
        "https://www.youtube.com/results?search_query=support+vector+machine+in+machine+learning"
    ],
    "K-Nearest Neighbors (KNN)": [
        knn_explanation,
        "./Instructions/Machine_Learning/Supervised/Classification/knn.png",
        "https://www.youtube.com/results?search_query=KNN+in+machine+learning"
    ],
    "Naive Bayes": [
        naive_bayes_explanation,
        "./Instructions/Machine_Learning/Supervised/Classification/nb.png",
        "https://www.youtube.com/results?search_query=naive+bayes+in+machine+learning"
    ],
}


SML_REG_MAPPER = {
    "Linear Regression": [
        linear_regression_markdown,
        "./Instructions/Machine_Learning/Supervised/Regression/lr.png",
        "https://www.youtube.com/results?search_query=Linear+regression+in+machine+learning"
    ],
    "Ridge Regression (L2 Regularization)": [
        ridge_regression_markdown,
        "./Instructions/Machine_Learning/Supervised/Regression/ridge_r.png",
        "https://www.youtube.com/results?search_query=Ridge+regression+in+machine+learning"
    ],
    "Lasso Regression (L1 Regularization)": [
        lasso_markdown_code,
        "./Instructions/Machine_Learning/Supervised/Regression/lr.png",
        "https://www.youtube.com/results?search_query=lasso+regression+in+machine+learning"
    ],
    "ElasticNet": [
        elastic_net_markdown,
        "./Instructions/Machine_Learning/Supervised/Regression/elasticnet.png",
        "https://www.youtube.com/results?search_query=elasticnet+in+machine+learning"
    ],
}


USML_CLUS_MAPPER = {
    "K Means": [
        kmeans_explanation,
        "./Instructions/Machine_Learning/Unsupervised/Clustering/kmeans.png",
        "https://www.youtube.com/results?search_query=kmeans+in+machine+learning"
    ],
    "Hierarchical Clustering": [
        hierarchial_markdown_code,
        "./Instructions/Machine_Learning/Unsupervised/Clustering/h_clus.png",
        "https://www.youtube.com/results?search_query=hierarchical+clustering+in+machine+learning"
    ],
    "DBSCAN (Density-Based Spatial Clustering of Applications with Noise)": [
        dbscan_markdown,
        "./Instructions/Machine_Learning/Unsupervised/Clustering/dbscan.png",
        "https://www.youtube.com/results?search_query=dbscan+in+machine+learning"
    ],
    "Gaussian Mixture Models (GMM)": [
        gmm_explanation,
        "./Instructions/Machine_Learning/Unsupervised/Clustering/gmm.png",
        "https://www.youtube.com/results?search_query=gmm+in+machine+learning"
    ],

}


USML_DIMRED_MAPPER = {
    "Principle Component Analysis (PCA)": [
        pca_markdown_code,
        "./Instructions/Machine_Learning/Unsupervised/Dimensionality_Reduction/pca.png",
        "https://www.youtube.com/results?search_query=PCA+in+machine+learning"
    ],
    "Singular Value Decomposition(SVD)": [
        svd_markdown_code,
        "./Instructions/Machine_Learning/Unsupervised/Dimensionality_Reduction/svd.png",
        "https://www.youtube.com/results?search_query=svd+in+machine+learning"
    ],
    "Linear Discriminant Analysis (LDA)": [
        lda_markdown_code,
        "./Instructions/Machine_Learning/Unsupervised/Dimensionality_Reduction/lda.png",
        "https://www.youtube.com/results?search_query=Linear+Discriminant+Analysis+(LDA)+in+machine+learning"
    ],

}


USML_ANADET_MAPPER = {
    "Z-Score": [
        zscore_markdown,
        "./Instructions/Machine_Learning/Unsupervised/Anomaly_Detection/zscore.png",
        "https://www.youtube.com/results?search_query=Z+score+for+anomaly+detection++in+machine+learning"
    ],


}
