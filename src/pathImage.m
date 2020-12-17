function pathImage(im)
%PATHIMAGE Summary of this function goes here
%   Detailed explanation goes here

[h, w] = size(im);

figure;
imr = im;

sx = -1;
sy = -1;
for sy = 1:h
    for sx = 1:w
        if imr(sx, sy) == 1
            queue = [sx sy];
            while size(queue, 1) > 0
                x = queue(1, 1);
                y = queue(1, 2);
                if imr(x, y) == 1
                    imr(x, y) = 0;
                    [ang, dist] = convert2AngleDist(y, x);
                    disp(ang + ";" + dist);
                    marked = insertMarker(mat2gray(im), [y, x]);
                    imshow(marked);
                    miniqueue = zeros(2, 0);
                    foundNearby = 0;
                    for j = y-1:y+1
                        for i = x-1:x+1
                            if imr(i, j) == 1
                                miniqueue = [i j; miniqueue];
                                foundNearby = 1;
                            end
                        end
                    end
                    if foundNearby == 0
                        disp("Stop dispensing");
                    end
                    queue = [queue(1, :); miniqueue; queue(2:end, :)];
                end
                queue = queue(2:end,:);
            end
        end
    end
end






end