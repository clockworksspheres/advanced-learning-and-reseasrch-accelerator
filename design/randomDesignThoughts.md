# First Attempt At Minimum Viable Product Brainstorming


## Start with Model View Controller type design, adding a few concepts learned and/or used from other projects

### Model

Model is an object and/or data structure that the view and controller operate on.  There will be a few models in this application programming model

### View

The View is the UI/Interface to the application programming model

Can be written any language, however may need language bridge to controller and other internal or back-end functionality

### Controller

The Controller is the engine of the application programming  model

#### Programming APIs to internal functionaity

#### CRUD

C Create
R Read
U Update
D Delete

An old ancronym used at times in the Database arena decades ago, but fits for writing data over not-REST interfaces, like databases, filesystem and similar type systems.

##### REST

Mostly for sending, but future release, duplicate programming APIs through REST type interface, to allow for a controller in a container or cloud, potentially separate from the data, and View.

#### Plugin system

Many programs/applications, and even firmware have modular plugin systems.

Going to check out the Napari Plugin Engine 2

#### I/O not otherwise specified

May consider prividing this functionality through the plugin system

* Printing
* Messaging systems (RabbitMQ, ZeroMQ, AmpQ, etc) - to send

