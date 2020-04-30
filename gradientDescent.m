function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
% number of training examples
m = length(y);
% to store the values of thetas
J_history = zeros(num_iters, 1);
% iterate till the number of epochs
for iter = 1:num_iters
    % store X
    x = X(:, 2) ;
    % hypothesis
    h = theta(1) + theta(2)*x ;
   
    % theta value calculation theta_0 = theta0 - learningRate(1/m)*sum(hypothesis-y)
    theta_0 = theta(1) - alpha * (1/m) * sum(h - y);
    % theta value calculation theta_1 = theta1 - learningRate(1/m)*sum(hypothesis-y) * x) 
    theta_1 = theta(2) - alpha * (1/m) * sum((h-y) .* x);
    
    % update theta
    theta = [theta_0 ; theta_1];
 
    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);
end
    % display the minimum cost
    fprintf("Minimum cost =");
    disp(min(J_history));
end