function monthextremcomp(filename,direction,dirBin)
%monthextrema(filename,direction,dirBin)
% 
% Author:       Ryan Starr
% Purpose:      This function imports wave data for a number of years and 
%               determines the monthly maximum significant wave heights for
%               a specified direction.
% CALL arg.     filename    :   name of file to import (expected format is
%                               space delimited with the following fields and one header line: 
%                               [ID YEAR MM DD HH LONG LAT Hmo DTp tmean wdvmn] where:
%                               ID      = station identifier
%                               YEAR    = 4-digit year
%                               MM      = month number
%                               DD      = day of the month
%                               HH      = hour of day
%                               LONG    = longitude of station
%                               LAT     = latitude of station in degrees North
%                               Hmo     = Significant wave height in meters
%                               DTp     = Peak spectral wave period
%                               tmean 	= Mean wave period in seconds calculated using the inverse first moment 
%                               wdvmn 	= Overall vector mean wave direction in degrees using Meteorological (MET) convention 
%               direction   :   (optional) wave direction of interest (in degrees, 0-360)
%               dirBin      :   (optional, default = 30 degrees) size of direction band 
%                               that will be centered around the direction of interest.

[ MM DD YEAR HH Hmo DTp wdvmn LONG LAT ] =...
    textread(filename,'%f %f %f %f %f %f %f %f %f','headerlines',1);

% check for optional arguments
direction=0;

if nargin < 3, direction = -1; end  % no direction specified


if direction~=-1
    % find the indexes for the specified direction and bin
    if minDir<0 
        DirIndex = find(wdvmn>=(360-minDir) | wdvmn<maxDir);
    else
        DirIndex= find(wdvmn>=minDir & wdvmn<maxDir);
    end
    
    % create new vectors for the specified direction and bin
    %ID = ID(DirIndex);
    YEAR = YEAR(DirIndex);
    MM = MM(DirIndex);
    DD = DD(DirIndex);
    HH = HH(DirIndex);
    LONG = LONG(DirIndex);
    LAT = LAT(DirIndex);
    Hmo = Hmo(DirIndex);
    DTp = DTp(DirIndex);
    wdvmn = wdvmn(DirIndex); 
end

% initialize values
recordCount = length(Hmo)
extremeIds = [];
extremeIndex = 0;
prevMonth = 0;
maxHmo = 0;

% loop through the records to find the monthly extreme Hmo indexes
for id = 1:recordCount
    month = MM(id);
    if month==prevMonth
        % check to see if this record is the monthly extreme
        if Hmo(id) > maxHmo
            maxHmo = Hmo(id);
            maxHmoId = id;
        end
    else
        % if this is not the first loop, set the previous month's extreme Hmo index
        if id > 1
            extremeIds(extremeIndex) = maxHmoId;
        end 
        % this is a new month, set maxHmo to the first record in month
        extremeIndex = extremeIndex+1;
        maxHmo = Hmo(id);
        maxHmoId = id;
    end
    prevMonth = month;
end 

% set the last month's extreme Hmo index
extremeIds(extremeIndex) = maxHmoId;



if direction~=-1
    filename = ('monthlyExtremedir.txt');
else
    filename = ('monthlyExtreme1.txt');
end
out = [YEAR(extremeIds) MM(extremeIds) DD(extremeIds) HH(extremeIds) ...
    Hmo(extremeIds) DTp(extremeIds) wdvmn(extremeIds)];
  
    
dlmwrite(filename,out,'delimiter',' ','precision',6)
