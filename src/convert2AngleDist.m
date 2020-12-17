function [angle,distance] = convert2AngleDist(ax,ay)
%CONVERT2ANGLEDIST Summary of this function goes here
%   Detailed explanation goes here
x = 256 - ay;
y = ax - 128;
angle = rad2deg(atan2(y, x));
distance = sqrt((x * x) + (y * y));
end

