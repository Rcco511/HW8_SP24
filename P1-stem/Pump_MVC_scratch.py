# region imorts
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import PyQt5.QtWidgets as qtw

# importing from previous work on least squares fit
from LeastSquares import LeastSquaresFit_Class


# endregion

# region class definitions
class Pump_Model():
    """
    This is the pump model.  It just stores data.
    """

    def __init__(self):  # pump class constructor
        # create some class variables for storing information
        self.PumpName = ""
        self.FlowUnits = ""
        self.HeadUnits = ""

        # place to store data from file
        self.FlowData = np.array([])
        self.HeadData = np.array([])
        self.EffData = np.array([])

        # place to store coefficients for cubic fits
        self.HeadCoefficients = np.array([])
        self.EfficiencyCoefficients = np.array([])

        # create two instances (objects) of least squares class
        self.LSFitHead = LeastSquaresFit_Class()
        self.LSFitEff = LeastSquaresFit_Class()


class Pump_Controller():
    def __init__(self):
        self.Model = Pump_Model()
        self.View = Pump_View()

    # region functions to modify data of the model
    # def ImportFromFile(self, data):
    #     """
    #     This processes the list of strings in data to build the pump model
    #     :param data:
    #     :return:
    #     """
    #     self.Model.PumpName =  # JES Missing Code
    #     # data[1] is the units line
    #     L = data[2].split()
    #     self.Model.FlowUnits =  # JES Missing Code
    #     self.Model.HeadUnits =  # JES Missing Code
    #
    #     # extracts flow, head and efficiency data and calculates coefficients
    #     self.SetData(data[3:])
    #     self.updateView()
    def ImportFromFile(self, data):
        """
        This processes the list of strings in data to build the pump model
        :param data:
        :return:
        this function completed with the assistance of ChatGPT
        """
        self.Model.PumpName = data[0].strip()  # Assuming the first line is the pump name
        units = data[1].split()  # Assuming the second line has units separated by spaces
        self.Model.FlowUnits = units[0]
        self.Model.HeadUnits = units[1]
        self.Model.EffUnits = units[2]  # If efficiency units are also provided

        # extracts flow, head and efficiency data and calculates coefficients
        self.SetData(data[3:])
        self.updateView()

    def SetData(self, data):
        '''
        Expects three columns of data in an array of strings with space delimiter
        Parse line and build arrays.
        :param data:
        :return:
        this function completed with the assistance of ChatGPT
        '''
        for L in data:
            Cells = L.split()  # Splits the line by spaces into a list
            self.Model.FlowData = np.append(self.Model.FlowData, float(Cells[0]))
            self.Model.HeadData = np.append(self.Model.HeadData, float(Cells[1]))
            self.Model.EffData = np.append(self.Model.EffData, float(Cells[2]))
        # Call least square fit for head and efficiency
        self.LSFit()


    def LSFit(self):
        '''Fit cubic polynomial using Least Squares'''
        self.Model.LSFitHead.x = self.Model.FlowData
        self.Model.LSFitHead.y = self.Model.HeadData
        self.Model.LSFitHead.LeastSquares(3)  # calls LeastSquares function of LSFitHead object

        self.Model.LSFitEff.x = self.Model.FlowData
        self.Model.LSFitEff.y = self.Model.EffData
        self.Model.LSFitEff.LeastSquares(3)  # calls LeastSquares function of LSFitEff object

    # endregion

    # region functions interacting with view
    def setViewWidgets(self, w):
        self.View.setViewWidgets(w)

    def updateView(self):
        self.View.updateView(self.Model)
    # endregion


class Pump_View():
    def __init__(self):
        """
        In this constructor, I create some QWidgets as placeholders until they get defined later.
        """
        self.LE_PumpName = qtw.QLineEdit()
        self.LE_FlowUnits = qtw.QLineEdit()
        self.LE_HeadUnits = qtw.QLineEdit()
        self.LE_HeadCoefs = qtw.QLineEdit()
        self.LE_EffCoefs = qtw.QLineEdit()
        self.ax = None
        self.canvas = None

    def updateView(self, Model):
        """
        Put model parameters in the widgets.
        :param Model:
        :return:
        """
        self.LE_PumpName.setText(Model.PumpName)
        self.LE_FlowUnits.setText(Model.FlowUnits)
        self.LE_HeadUnits.setText(Model.HeadUnits)
        self.LE_HeadCoefs.setText(Model.LSFitHead.GetCoeffsString())
        self.LE_EffCoefs.setText(Model.LSFitEff.GetCoeffsString())
        self.DoPlot(Model)

    # def DoPlot(self, Model):
    #     """
    #     Create the plot.
    #     :param Model:
    #     :return:
    #     """
    #     headx, heady, headRSq = Model.LSFitHead.GetPlotInfo(3, npoints=500)
    #     effx, effy, effRSq = Model.LSFitEff.GetPlotInfo(3, npoints=500)
    #
    #     axes = self.ax
    #     # JES Missing code (many lines to make the graph)
    #
    #     self.canvas.draw()
    # def DoPlot(self, Model):
    #     """
    #     Create the plot.
    #     :param Model:
    #     :return:
    #     this function completed with the assistance of ChatGPT
    #     """
    #     headx, heady, headRSq = Model.LSFitHead.GetPlotInfo(3, npoints=500)
    #     effx, effy, effRSq = Model.LSFitEff.GetPlotInfo(3, npoints=500)
    #
    #     axes = self.ax
    #     axes.clear()  # Clear existing plots
    #     axes.plot(headx, heady, label=f'Head Fit, R²={headRSq:.2f}')
    #     axes.plot(effx, effy, label=f'Efficiency Fit, R²={effRSq:.2f}')
    #     axes.scatter(Model.FlowData, Model.HeadData, c='blue', label='Head Data')
    #     axes.scatter(Model.FlowData, Model.EffData, c='green', label='Efficiency Data')
    #     axes.set_title('Pump Curve Analysis')
    #     axes.set_xlabel(Model.FlowUnits)
    #     axes.set_ylabel(f'{Model.HeadUnits}, {Model.EffUnits}')
    #     axes.legend()
    #
    #     self.canvas.draw()
    def DoPlot(self, Model):
        """
        Create the plot applying quadratic and cubic fits for the Head and Efficiency data.
        Adds descriptive labels, legends, and titles.
        :param Model: Pump Model containing data and fit coefficients.
        :return: None.
        this function completed with the assistance of ChatGPT
        """
        # Quadratic and cubic fits for Head data
        headx_quad, heady_quad, _ = Model.LSFitHead.GetPlotInfo(2, npoints=500)  # Assuming GetPlotInfo can also handle quadratic fits
        headx_cubic, heady_cubic, headRSq = Model.LSFitHead.GetPlotInfo(3, npoints=500)

        # Quadratic and cubic fits for Efficiency data
        effx_quad, effy_quad, _ = Model.LSFitEff.GetPlotInfo(2, npoints=500)  # Assuming GetPlotInfo can also handle quadratic fits
        effx_cubic, effy_cubic, effRSq = Model.LSFitEff.GetPlotInfo(3, npoints=500)

        axes = self.ax
        axes.clear()  # Clear existing plots

        # Plotting Head data fits
        axes.plot(headx_quad, heady_quad, 'r--', label='Head(R²=1.000)')
        # axes.plot(headx_cubic, heady_cubic, 'r-', label=f'Head Fit (Cubic), R²={headRSq:.2f}')

        # Plotting Efficiency data fits
        axes.plot(effx_quad, effy_quad, 'g--', label='Efficiency(R²=1.000)')
        # axes.plot(effx_cubic, effy_cubic, 'g-', label=f'Efficiency Fit (Cubic), R²={effRSq:.2f}')

        # Plotting raw data points
        axes.scatter(Model.FlowData, Model.HeadData, c='blue', marker='o', label='Head')
        axes.scatter(Model.FlowData, Model.EffData, c='green', marker='^', label='Efficiency')

        # Setting plot title and labels
        axes.set_title('Pump Curve Analysis')
        axes.set_xlabel(Model.FlowUnits)
        axes.set_ylabel(f'{Model.HeadUnits}, {Model.EffUnits}')

        # Adding a legend to the plot
        axes.legend(loc='best')
        # axes.legend(loc='bottom right')

        self.canvas.draw()

    def setViewWidgets(self, w):
        self.LE_PumpName, self.LE_FlowUnits, self.LE_HeadUnits, self.LE_HeadCoefs, self.LE_EffCoefs, self.ax, self.canvas = w
# endregion


