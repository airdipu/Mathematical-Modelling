function [x,y,i]= Rosenbrock
% Descent procedure

% Set the start point:
% x = 0.5*(rand(2,1) - 0.5);
x = [-1.2;1];

% Parameter for the termination iteration:
maxit = 10^5; % maximum Iteration
tol = 10^(-5); % Tolerance

% Here begins the process
i = 0; % Iteration count
               
[x1,x2] = meshgrid(-1.5:.05:1.5);
z = (1-x1).^2 + 100*(-x1.^2 + x2).^2;
contour(x1, x2, z, 20)
hold on

while (i < maxit)  && (norm(DRosenbrock(x)') > tol) 
    s = -(DRosenbrock(x))'; % Descent direction 
    sigma = 0.00125; % Step size
    xnew = x + sigma * s; % Update
    
    % plot
    plot([x(1) xnew(1)],[x(2) xnew(2)])
    
    i = i+1; 
    x = xnew;
end

y = Rosenbrock(x);

i
end



% Here calculation of Rosenbrock function
function y = Rosenbrock( x )
y = (1 - x(1))^2 + 100 * (- x(1)^2 + x(2))^2;
end

function u = DRosenbrock( x )
u = [ -2*(1 - x(1)) - 400*x(1)*(-x(1)^2 + x(2)) , 200*(-x(1)^2 + x(2)) ];
end
