# -*- coding: utf-8 -*-
"""
Created on June 20 2018

@author: kushal

Chatzigeorgiou Group
Sars International Centre for Marine Molecular Biology

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

import abc
import numpy as np
from PyQt5 import QtWidgets
from .... import pyqtgraphCore as pg
# from typing import Type, TypeVar
from ....common import get_proj_config, NoProjectOpen, InheritDocs
from warnings import warn
from copy import deepcopy
from typing import Union


class _AbstractBaseROI(metaclass=InheritDocs):
    """
    Abstract base class defining an ROI that works with the ROIList and ROI Managers.
    Inherit from this or BaseROI to make a new ROI class
    """
    @abc.abstractmethod
    def __init__(self, curve_plot_item: pg.PlotDataItem, view_box: pg.ViewBox, state: Union[dict, None]):
        """
        Minimum required attributes

        :param curve_plot_item: The plot item that is used for display the curves in the viewer
        :param view_box:        ViewBox containing the image sequence, used for overlaying the ROIs on top of the image
        :param state:           ROI state, used for restoring the ROIs. Pass None is not restoring an ROI from a state dict
        """
        pass

    @property
    @abc.abstractmethod
    def curve_data(self) -> tuple:
        """
        The curve data for this ROI

        :return: (x, y), [np.ndarray, np.ndarray]
        :rtype: tuple
        """
        pass

    @curve_data.setter
    @abc.abstractmethod
    def curve_data(self, data: tuple):
        """
        Set the curve data for this ROI

        :param data: (x, y), [np.ndarray, np.ndarray]
        """
        pass

    @abc.abstractmethod
    def get_roi_graphics_object(self) -> QtWidgets.QGraphicsObject:
        """Get the QGraphicsObject used for visualization of the spatial localization of the ROI"""
        pass

    @abc.abstractmethod
    def set_roi_graphics_object(self, *args, **kwargs):
        """Set the QGraphicsObject used for visualization of the spatial localization of the ROI"""
        pass

    @abc.abstractmethod
    def reset_color(self):
        """Reset the color of this ROI back to the original color"""
        pass

    @abc.abstractmethod
    def set_original_color(self, color):
        """
        Set the original color for this ROI

        :param color: 1D numpy array of 4 floating point numbers (range 0 - 255) in RBGA format, [R, G, B, A]
        """
        pass

    @abc.abstractmethod
    def get_color(self) -> np.ndarray:
        """
        Get the current color of this ROI

        :return: 1D numpy array of 4 floating point numbers (range 0 - 255) in RBGA format, [R, G, B, A]
        :rtype: np.ndarray
        """
        pass

    @abc.abstractmethod
    def set_color(self, color, *args, **kwargs):
        """
        Set the current color of this ROI

        :param color: 1D numpy array of 4 floating point numbers (range 0 - 255) in RBGA format, [R, G, B, A]
        """
        pass

    @abc.abstractmethod
    def set_text(self, text: str):
        """Not implemented"""
        pass

    @abc.abstractmethod
    def set_tag(self, roi_def: str, tag: str):
        """
        Set a tag for the passed roi_def

        :param roi_def: The ROI_DEF that should be tagged
        :param tag:     The tag to label for the passed ROI_DEF/ROI Type
        """
        pass

    @abc.abstractmethod
    def get_tag(self, roi_def) -> str:
        """
        Get the tag that is set to the passed 'roi_def'

        :rtype: str
        """
        pass

    @abc.abstractmethod
    def get_all_tags(self) -> dict:
        """
        Get all the tags for all the ROI_DEFs

        :rtype: dict
        """
        pass

    @abc.abstractmethod
    def add_to_viewer(self):
        """Add this ROI to the viewer."""
        pass

    @abc.abstractmethod
    def remove_from_viewer(self):
        """Remove this ROI from the viewer"""
        pass

    @abc.abstractmethod
    def to_state(self):
        """Get the current state for this ROI so that it can be restored later"""
        pass

    @classmethod
    @abc.abstractmethod
    def from_state(cls, curve_plot_item: pg.PlotDataItem, view_box: pg.ViewBox, state: dict):
        """
        Restore this ROI from a state

        :param curve_plot_item: The plot item that is used for display the curves in the viewer
        :param view_box:        ViewBox containing the image sequence, used for overlaying the ROIs on top of the image
        :param state:           ROI state, used for restoring the ROIs. Pass None is not restoring an ROI from a state dict
        """
        pass


class BaseROI(_AbstractBaseROI):
    """
    A base class that is used by ManualROI and CNMFEROI
    Inherit from this to make a new ROI class
    """
    def __init__(self, curve_plot_item: pg.PlotDataItem, view_box: pg.ViewBox, state: Union[dict, None] = None):
        """
        Instantiate common attributes

        :param curve_plot_item: The plot item that is used for display the curves in the viewer
        :param view_box:        ViewBox containing the image sequence, used for overlaying the ROIs on top of the image
        :param state:           ROI state, used for restoring the ROIs. Pass None is not restoring an ROI from a state dict

        """
        super().__init__(curve_plot_item, view_box, state)
        if isinstance(curve_plot_item, pg.PlotDataItem):
            self.curve_plot_item = curve_plot_item
            self.curve_plot_item.setZValue(1)
        else:
            self.curve_plot_item = None

        if state is None:
            try:
                # Set the Tags list from the project configuration
                roi_defs = get_proj_config().options('ROI_DEFS')
                self._tags = dict.fromkeys(roi_defs)
            except NoProjectOpen as e:
                self._tags = {}
                # If a project isn't open
                warn('BaseROI subclass instance cannot load ROI_DEFS, no Project open.')
        else:
            # Restore states
            self._tags = state['tags']
            self.curve_data = state['curve_data']

        self.view_box = view_box
        self.roi_graphics_object = None
        self._color = None
        self._original_color = None

    @property
    def curve_data(self) -> tuple:
        return self.curve_plot_item.getData()

    @curve_data.setter
    def curve_data(self, data: tuple):
        """

        :rtype: tuple
        """
        if self.curve_plot_item is None:
            return
        self.curve_plot_item.setData(x=data[0], y=data[1])

    @property
    def zValue(self) -> int:
        """ZValue of the curve plot graphics object and roi_graphics_object"""
        return self._zValue

    @zValue.setter
    def zValue(self, val: int):
        self._zValue = val

    def get_roi_graphics_object(self) -> QtWidgets.QGraphicsObject:
        pass

    def set_roi_graphics_object(self, *args, **kwargs):
        pass

    def reset_color(self):
        self.set_color(self._original_color)

    def set_original_color(self, color):
        self._original_color = color
        self.reset_color()

    def get_color(self):
        return self._color

    def set_color(self, color: Union[np.ndarray, str], *args, **kwargs):
        pen = pg.mkPen(color, *args, **kwargs)
        self.roi_graphics_object.setPen(pen)
        self.curve_plot_item.setPen(pen)
        if isinstance(self.roi_graphics_object, pg.ScatterPlotItem):
            self.roi_graphics_object.setBrush(pg.mkBrush(color, *args, **kwargs))
        self._color = color

    def set_text(self, text: str):
        text_item = pg.TextItem(text)
        # self.view_box.addItem()

    def set_tag(self, roi_def: str, tag: str):
        self._tags[roi_def] = tag

    def get_tag(self, roi_def) -> str:
        if self._tags[roi_def] is None:
            return ''
        return self._tags[roi_def]

    def get_all_tags(self) -> dict:
        d = deepcopy(self._tags)
        for key in d.keys():
            if d[key] is None:
                d[key] = ''
        return d

    def add_to_viewer(self):
        self.view_box.addItem(self.get_roi_graphics_object())

    def remove_from_viewer(self):
        roi = self.get_roi_graphics_object()
        self.view_box.removeItem(roi)
        if self.curve_plot_item is not None:
            self.curve_plot_item.clear()
        del self.curve_plot_item
        del roi

    def to_state(self):
        """Must be implemented in subclass"""
        raise NotImplementedError("Must be implemented in subclasses")

    @classmethod
    def from_state(cls, curve_plot_item: pg.PlotDataItem, view_box: pg.ViewBox, state: dict):
        raise NotImplementedError("Must be implemented in subclasses")


class ManualROI(BaseROI):
    """A class manually drawn ROIs"""
    def __init__(self, curve_plot_item: pg.PlotDataItem,
                 roi_graphics_object: pg.ROI,
                 view_box: pg.ViewBox,
                 state: Union[dict, None] = None):
        """
        :type state: dict
        """
        assert isinstance(roi_graphics_object, pg.ROI)

        super(ManualROI, self).__init__(curve_plot_item, view_box, state)

        self.set_roi_graphics_object(roi_graphics_object)

        if state is not None:
            self.add_to_viewer()
            self._set_roi_graphics_object_state(state['roi_graphics_object_state'])

    def get_roi_graphics_object(self) -> pg.ROI:
        return self.roi_graphics_object

    def set_roi_graphics_object(self, graphics_object: pg.ROI):
        self.roi_graphics_object = graphics_object

    def _set_roi_graphics_object_state(self, state):
        self.roi_graphics_object.setState(state)

    def to_state(self):
        if isinstance(self.roi_graphics_object, pg.PolyLineROI):
            shape = 'PolyLineROI'
        elif isinstance(self.roi_graphics_object, pg.EllipseROI):
            shape = 'EllipseROI'

        state = {'curve_data': self.curve_data,
                 'shape': shape,
                 'roi_graphics_object_state': self.roi_graphics_object.saveState(),
                 'tags': self.get_all_tags(),
                 'roi_type': 'ManualROI'
                 }
        return state

    @staticmethod
    def get_generic_roi_graphics_object(shape: str, dims: tuple) -> pg.ROI:
        """Get a generic pg.ROI instance to add to the viewer. Its state can later be set from a saved state or it can be modified by the user"""
        x = dims[0]
        y = dims[1]

        if shape == 'PolyLineROI':
            roi_graphics_object = pg.PolyLineROI([[0, 0],
                                                  [int(0.1 * x), 0],
                                                  [int(0.1 * x), int(0.1 * y)],
                                                  [0, int(0.1 * y)]],
                                                 closed=True, pos=[0, 0], removable=True)
            return roi_graphics_object

        elif shape == 'EllipseROI':
            roi_graphics_object = pg.EllipseROI(pos=[0, 0], size=[x, y], removable=True)
            return roi_graphics_object

    @classmethod
    def from_state(cls, curve_plot_item: pg.PlotDataItem, view_box: pg.ViewBox, state: dict):
        roi_graphics_object = ManualROI.get_generic_roi_graphics_object(state['shape'], (10, 10))
        return cls(curve_plot_item=curve_plot_item, roi_graphics_object=roi_graphics_object, view_box=view_box, state=state)

    @classmethod
    def from_positions(cls, curve_plot_item: pg.PlotDataItem, view_box: pg.ViewBox, positions: list):
        """
        From a list of positions. Used if importing ImageJ ROIs, can be used for other purposes as well.

        :param positions: list of (x, y) tuples; [(x1, y1), (x2, y2), ... (xn, yn)]
        """
        roi_graphics_object = pg.PolyLineROI(positions=positions, closed=True, removable=True)
        return cls(curve_plot_item=curve_plot_item, roi_graphics_object=roi_graphics_object, view_box=view_box)


class CNMFROI(BaseROI):
    """A class for ROIs imported from CNMF(E) output data"""
    def __init__(self, curve_plot_item: pg.PlotDataItem,
                 view_box: pg.ViewBox, cnmf_idx: int = None,
                 curve_data=None, contour=None, state: Union[dict, None] = None, **kwargs):
        """
        Instantiate attributes.

        :type: curve_data:  np.ndarray
        :param curve_data:  1D numpy array of y values
        :type  contour:     np.ndarray
        :type  state:       dict
        :param cnmf_idx:    original index of the ROI from cnmf idx_components
        """
        super(CNMFROI, self).__init__(curve_plot_item, view_box, state)

        self.roi_xs = np.empty(0)  #: numpy array of the x values of the ROI's spatial coordinates
        self.roi_ys = np.empty(0)  #: numpy array of the y values of the ROI's spatial coordinates

        if 'raw_min_max' in kwargs.keys():
            self.raw_min_max = kwargs.pop('raw_min_max')
        else:
            self.raw_min_max = None

        if state is None:
            self.set_roi_graphics_object(contour)
            self.set_curve_data(curve_data)
            self.cnmf_idx = cnmf_idx  #: original index of the ROI from cnmf idx_components
        else:
            self._restore_state(state)

    def set_curve_data(self, y_vals):
        """Set the curve data"""
        xs = np.arange(len(y_vals))
        self.curve_data = [xs, y_vals]

    def _restore_state(self, state):
        self.roi_xs = state['roi_xs']
        self.roi_ys = state['roi_ys']

        self._create_scatter_plot()
        # self.curve_data = state['curve_data']
        self.cnmf_idx = state['cnmf_idx']

        if 'raw_min' in state.keys() and 'raw_max' in state.keys():
            self.raw_min = state.pop('raw_min')
            self.raw_max = state.pop('raw_max')
        else:
            self.raw_min = None
            self.raw_max = None

    def get_roi_graphics_object(self) -> pg.ScatterPlotItem:
        if self.roi_graphics_object is None:
            raise AttributeError('Must call set_roi_graphics_object() first')

        return self.roi_graphics_object

    def set_roi_graphics_object(self, contour: dict):
        cors = contour['coordinates']
        cors = cors[~np.isnan(cors).any(axis=1)]

        xs = cors[:, 0].flatten()
        ys = cors[:, 1].flatten()

        self.roi_xs = xs.astype(int)
        self.roi_ys = ys.astype(int)

        self._create_scatter_plot()

    def _create_scatter_plot(self):
        """Create the scatter plot that is used for visualization of the spatial localization"""
        self.roi_graphics_object = pg.ScatterPlotItem(self.roi_xs, self.roi_ys, symbol='s', size=1)

    def to_state(self) -> dict:
        state = {'roi_xs':      self.roi_xs,
                 'roi_ys':      self.roi_ys,
                 'curve_data':  self.curve_data,
                 'tags':        self.get_all_tags(),
                 'roi_type':    'CNMFROI',
                 'cnmf_idx':    self.cnmf_idx,
                 'raw_min_max': self.raw_min_max
                 }
        return state

    @classmethod
    def from_state(cls, curve_plot_item: pg.PlotDataItem, view_box: pg.ViewBox, state: dict):
        return cls(curve_plot_item=curve_plot_item, view_box=view_box, state=state)
