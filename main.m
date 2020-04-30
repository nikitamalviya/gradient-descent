%% --- DRIVER CODE ---
%% load dataset
data = load('data.txt');
X = data(:, 1);
y = data(:, 2);
%% plot data
fprintf('Plotting Data ...\n')
plotData(X, y);

%% Cost and Gradient descent
% Add a column of ones to x (x0 = 1)
X = [ones(m, 1), data(:,1)]; 
theta = zeros(2, 1); % initialize fitting parameters

% Some gradient descent settings
iterations = 1500;
alpha = 0.01;
% number of training examples
m = length(y);
% run gradient descent
theta = gradientDescent(X, y, theta, alpha, iterations);
