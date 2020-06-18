function varargout = soru2(varargin)
% SORU2 MATLAB code for soru2.fig
%      SORU2, by itself, creates a new SORU2 or raises the existing
%      singleton*.
%
%      H = SORU2 returns the handle to a new SORU2 or the handle to
%      the existing singleton*.
%
%      SORU2('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in SORU2.M with the given input arguments.
%
%      SORU2('Property','Value',...) creates a new SORU2 or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before soru2_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to soru2_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help soru2

% Last Modified by GUIDE v2.5 18-Jun-2020 14:25:33

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @soru2_OpeningFcn, ...
                   'gui_OutputFcn',  @soru2_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before soru2 is made visible.
function soru2_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to soru2 (see VARARGIN)

% Choose default command line output for soru2
handles.output = hObject;
handles.zaman=0;
handles.tumsinyal=0;
handles.slider=0;
handles.sekil='-'
handles.renk='b'
handles.conf=''
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes soru2 wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = soru2_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
  [file, path] = uigetfile ( '*.mat' ) 
  if isequal(file,0)
    disp('User selected Cancel')
  else
    s=load(fullfile(path,file))
    
    handles.zaman=s.zaman;
    handles.tumsinyal=s.tumsinyal;
    guidata(hObject,handles)
     % XXX is variable contains in you mat file
                
  end


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
zaman=handles.zaman;
sinyal=handles.tumsinyal;
handles.conf= strcat(handles.renk,handles.sekil)
plot(zaman,sinyal,handles.conf)
guidata(hObject,handles)
xlim([0 1]) 


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
closereq(); 

% --- Executes on slider movement.
function slider1_Callback(hObject, eventdata, handles)
% hObject    handle to slider1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
guidata(hObject,handles)
handles.slider=get(hObject,'Value')/90;

plot(handles.zaman,handles.tumsinyal,handles.conf)
xlim([handles.slider-1 handles.slider]) 


% --- Executes during object creation, after setting all properties.
function slider1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to slider1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on selection change in listbox1.
function listbox1_Callback(hObject, eventdata, handles)
% hObject    handle to listbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns listbox1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from listbox1

contents = cellstr(get(hObject,'String'));
secim=contents{get(hObject,'Value')}
if (strcmp(secim,'Circle')==1)
    handles.sekil=' o'
elseif(strcmp(secim,'Asterisk')==1)
    handles.sekil=' +'
elseif(strcmp(secim,'Point')==1)
    handles.sekil=' .'
elseif(strcmp(secim,'Cross')==1)
    handles.sekil=' x'
elseif(strcmp(secim,'Square')==1)
    handles.sekil=' s'
elseif(strcmp(secim,'Diamond')==1)
    handles.sekil=' d'
else
    handles.sekil=' .'
end

guidata(hObject,handles)




% --- Executes during object creation, after setting all properties.
function listbox1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to listbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on selection change in listbox3.
function listbox3_Callback(hObject, eventdata, handles)
% hObject    handle to listbox3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns listbox3 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from listbox3

contents = cellstr(get(hObject,'String'));
secim=contents{get(hObject,'Value')}
handles.renk=secim;
guidata(hObject,handles)

% --- Executes during object creation, after setting all properties.
function listbox3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to listbox3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
