from StickDeflectionWidget import StickDeflectionWidget
from ChannelWidget import ChannelWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MotorsPage(QWidget):
    def __init__(self):
        super(MotorsPage, self).__init__()

        # Create the Motor page UI here

        # Constants for UI declared here
        M1_THROTTLE_PERCENTAGE = 25
        M2_THROTTLE_PERCENTAGE = 50
        M3_THROTTLE_PERCENTAGE = 75
        M4_THROTTLE_PERCENTAGE = 100

        M1_MOTOR_OUTPUT = 10
        M2_MOTOR_OUTPUT = 20
        M3_MOTOR_OUTPUT = 30
        M4_MOTOR_OUTPUT = 40

        M1_CURRENT_DRAW = 10
        M2_CURRENT_DRAW = 20
        M3_CURRENT_DRAW = 30
        M4_CURRENT_DRAW = 40

        # Create the layouts for the throttle % UI
        body_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        channel_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()
        throttle_layout = QVBoxLayout()
        throttle_percentage_layout = QHBoxLayout()
        m1_layout = QVBoxLayout()
        m2_layout = QVBoxLayout()
        m3_layout = QVBoxLayout()
        m4_layout = QVBoxLayout()

        # Motor 1 Throttle %
        self.m1ProgressBar = QProgressBar(self)
        self.m1ProgressBar.setValue(M1_THROTTLE_PERCENTAGE)
        self.m1ProgressBar.setOrientation(Qt.Vertical)

        m1_layout.addWidget( QLabel("Motor 1") )
        m1_layout.addWidget(self.m1ProgressBar)
        m1_layout.addWidget( QLabel(f"{M1_THROTTLE_PERCENTAGE} %") )

        # Motor 2 Throttle %
        self.m2ProgressBar = QProgressBar(self)
        self.m2ProgressBar.setValue(M2_THROTTLE_PERCENTAGE)
        self.m2ProgressBar.setOrientation(Qt.Vertical)

        m2_layout.addWidget( QLabel("Motor 2") )
        m2_layout.addWidget(self.m2ProgressBar)
        m2_layout.addWidget( QLabel(f"{M2_THROTTLE_PERCENTAGE} %") )

        # Motor 3 Throttle %
        self.m3ProgressBar = QProgressBar(self)
        self.m3ProgressBar.setValue(M3_THROTTLE_PERCENTAGE)
        self.m3ProgressBar.setOrientation(Qt.Vertical)

        m3_layout.addWidget( QLabel("Motor 3") )
        m3_layout.addWidget(self.m3ProgressBar)
        m3_layout.addWidget( QLabel(f"{M3_THROTTLE_PERCENTAGE} %") )

        self.m4ProgressBar = QProgressBar(self)
        self.m4ProgressBar.setValue(M4_THROTTLE_PERCENTAGE)
        self.m4ProgressBar.setOrientation(Qt.Vertical)

        # Motor 4 Throttle %
        m4_layout.addWidget( QLabel("Motor 4") )
        m4_layout.addWidget(self.m4ProgressBar)
        m4_layout.addWidget( QLabel(f"{M4_THROTTLE_PERCENTAGE} %") )

        # Add Throttle % to the layout
        throttle_percentage_layout.addLayout(m1_layout)
        throttle_percentage_layout.addLayout(m2_layout)
        throttle_percentage_layout.addLayout(m3_layout)
        throttle_percentage_layout.addLayout(m4_layout)

        # Add title to throttle percentage display
        throttle_layout.addWidget( QLabel("Throttle Percentage") )
        throttle_layout.addLayout(throttle_percentage_layout)

        # Create the layouts for the Motor output UI
        motor_output_layout = QVBoxLayout()
        m1_output_layout = QVBoxLayout()
        m2_output_layout = QVBoxLayout()
        m3_output_layout = QVBoxLayout()
        m4_output_layout = QVBoxLayout()

        m1_output_layout.addWidget( QLabel("Motor 1 Output") )
        m1_output_layout.addWidget( QLabel(f"Motor Output: {M1_MOTOR_OUTPUT}"))

        m2_output_layout.addWidget( QLabel("Motor 2 Output") )
        m2_output_layout.addWidget( QLabel(f"Motor Output: {M2_MOTOR_OUTPUT}"))

        m3_output_layout.addWidget( QLabel("Motor 3 Output") )
        m3_output_layout.addWidget( QLabel(f"Motor Output: {M3_MOTOR_OUTPUT}"))

        m4_output_layout.addWidget( QLabel("Motor 4 Output") )
        m4_output_layout.addWidget( QLabel(f"Motor Output: {M4_MOTOR_OUTPUT}"))

        motor_output_layout.addSpacing(20)
        motor_output_layout.addLayout(m1_output_layout)
        motor_output_layout.addSpacing(15)
        motor_output_layout.addLayout(m2_output_layout)
        motor_output_layout.addSpacing(15)
        motor_output_layout.addLayout(m3_output_layout)
        motor_output_layout.addSpacing(15)
        motor_output_layout.addLayout(m4_output_layout)

        # Add layouts on the top of the screen to top layout
        top_layout.addLayout(throttle_layout)
        top_layout.addSpacing(60)
        top_layout.addLayout(motor_output_layout)

        # Create the layouts for stick deflection UI
        l_pbar_layout = QVBoxLayout()
        lx_axis_layout = QHBoxLayout()
        ly_axis_layout = QHBoxLayout()
        lz_axis_layout = QHBoxLayout()

        self.lx_rot_pbar = QProgressBar(self)
        self.lx_rot_pbar.setValue(10)

        self.ly_rot_pbar = QProgressBar(self)
        self.ly_rot_pbar.setValue(20)

        self.lz_axis_pbar = QProgressBar(self)
        self.lz_axis_pbar.setValue(30)

        lx_axis_layout.addWidget(QLabel("X Rotation"))
        lx_axis_layout.addWidget(self.lx_rot_pbar)

        ly_axis_layout.addWidget(QLabel("Y Rotation"))
        ly_axis_layout.addWidget(self.ly_rot_pbar)

        lz_axis_layout.addWidget(QLabel("Z Axis      "))
        lz_axis_layout.addWidget(self.lz_axis_pbar)

        l_pbar_layout.addLayout(lx_axis_layout)
        l_pbar_layout.addLayout(ly_axis_layout)
        l_pbar_layout.addLayout(lz_axis_layout)

        bottom_layout.addLayout(l_pbar_layout)

        # Add stick deflection
        self.right_stick_deflection = StickDeflectionWidget("Right Stick", 75, 75)
        self.left_stick_deflection = StickDeflectionWidget("Left Stick", 75, 75)
        
        bottom_layout.addWidget(self.right_stick_deflection)
        bottom_layout.addWidget(self.left_stick_deflection)

        # Add component layouts to final body layout
        left_layout.addLayout(top_layout)
        left_layout.addSpacing(25)
        left_layout.addLayout(bottom_layout)

        # Add channel layout
        channel_layout.addWidget( QLabel("Channels") )
        channel_layout.addWidget( ChannelWidget("Channel 1 ", "50") )
        channel_layout.addWidget( ChannelWidget("Channel 2 ", "50") )
        channel_layout.addWidget( ChannelWidget("Channel 3 ", "50") )
        channel_layout.addWidget( ChannelWidget("Channel 4 ", "50") )
        channel_layout.addWidget( ChannelWidget("Channel 5 ", "50") )
        channel_layout.addWidget( ChannelWidget("Channel 6 ", "50") )
        channel_layout.addWidget( ChannelWidget("Channel 7 ", "50") )
        channel_layout.addWidget( ChannelWidget("Channel 8 ", "50") )
        channel_layout.addWidget( ChannelWidget("Channel 9 ", "50") )
        channel_layout.addWidget( ChannelWidget("Channel 10", "50") )
        channel_layout.addWidget( ChannelWidget("Channel 11", "50") )
        channel_layout.addWidget( ChannelWidget("Channel 12", "50") )
        channel_layout.addWidget( ChannelWidget("Channel 13", "50") )
        channel_layout.addWidget( ChannelWidget("Channel 14", "50") )
        channel_layout.addWidget( ChannelWidget("Channel 15", "50") )
        channel_layout.addWidget( ChannelWidget("Channel 16", "50") )

        body_layout.addLayout(left_layout)
        body_layout.addSpacing(50)
        body_layout.addLayout(channel_layout)

        self.setLayout(body_layout)
