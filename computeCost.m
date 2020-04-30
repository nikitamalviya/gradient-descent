function J = computeCost(X, y, theta)
% compute cost for linear regression
% computes the cost of using theta as a
% parameter for linear regression to fit the data points in X and y
% initialize some useful values
m = length(y); % number of training examples
J = 0;
% calculate prediction value
prediction = X*theta;
% calculate mean squared value
squared_error = (prediction-y).^2;
% compute the cost
J = 1/(2*m) * sum(squared_error);
end