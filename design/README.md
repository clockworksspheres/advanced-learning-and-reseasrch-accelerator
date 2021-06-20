# learning-and-research-accelerator

## WARNING

1. This directory is intended to be used as a loose ideas of future direction for the project.

2. The further the modification date of this file is from the current date - the less likely these file match the actual details of the design.  Design changes are often made to released software projects (in general) where design documents may not be updated or curated.

## Purpose

The purpose of this software is to provide frameworks and automation around the learning and research processes, that came together for me when I started a Doctor in Computer Science(DCS) program.  Sadly I was unable to complete the program for a variety of reasons, but some awesome learning still came out of it.

The [Kerko](https://github.com/whiskyechobravo/kerko) project inspired this project, Object Oriented Programming(OOP) principles, the Von Neumann Machine, along with the experience project developers and maintainers have in ETL, file parsing and web scraping.

## Design and Architecture

### visualize

It is important for me, when designing software to visualize how to break down the project into atomic parts, in standard object oriented patterns, diagrams of the atomic parts and how they might interact, use cases, etc.  From different points of view as well.  From a client view, server view, how a user might see the components, how someone maintaining the project might see the components, how other developers might see the components, how management might see the components, how marketing might see the components... Sometimes, in addition to one or more of those perspectives, different elevations of abstraction as well.  a 40,000 foot view, 30k foot view, 20k foot view 100 foot view, etc.  The purpose being to solidify the design for the different stakeholders.  Note that a small change at one level can mean changes, possibly big ones, at other elevations of perspective.

Using [UML](https://www.uml.org/what-is-uml.htm) may or may not be useful during early parts of the design. Some [useful UML tools can be found below](#uml-tools).

The real reason for the diagrams are two fold - know what and how to design the project, and "communication" to make sure that design to all the stakeholders are on the same page.

A napkin sketch might be enough for a project.  may not even be necessary to put into source code control.  Other projects might be more complicated, and have many stakeholders that need to buy into the project - needing change control boards to manage changes to the project.  The need for design documents for any project is a sliding scale between, possibly beyond these two examples.

The diagrams provided in this repo started, and continue to evolve towards the multi altitude view of the project, as it has a more complex and extensible design than many projects I've worked on in the past.
### Pattern

Inspiration for this pattern came from the Model View Controller (MVC) pattern, melded with the von neumann computer model, as well as *nix commands that are generally controlled by a "subcommand"[1](https://en.wikipedia.org/wiki/Sub_Command),[2](https://en.wiktionary.org/wiki/subcommand),  like [git](https://git.github.io/htmldocs/git.html), [launchctl](https://ss64.com/osx/launchctl.html), [systemctl](https://www.commandlinux.com/man-page/man1/systemctl.1.html),  and also the idea of [Open Container Initiative (OCI)](https://opencontainers.org/) [container registries](https://searchcloudcomputing.techtarget.com/definition/container-registry).

Export of the initial vym file of this pattern: 

![vym file of this pattern](https://github.com/clockworksspheres/learning-and-reseasrch-accelerator/blob/main/design/learningNresearchAccelleratorRegistry_2021-06-19_2039.png).


## References

### Model View Controller (MVC) pattern

* []()

* []()


### Von Neumann machine 

* [https://www.cs.utexas.edu/users/fussell/courses/cs310h/lectures/Lecture_9-310h.pdf](https://www.cs.utexas.edu/users/fussell/courses/cs310h/lectures/Lecture_9-310h.pdf)

* [http://www.c-jump.com/CIS77/CPU/VonNeumann/lecture.html](http://www.c-jump.com/CIS77/CPU/VonNeumann/lecture.html)

* [https://www.computerscience.gcse.guru/theory/von-neumann-architecture](https://www.computerscience.gcse.guru/theory/von-neumann-architecture)

* [https://history-computer.com/john-von-neumann-biography-history-and-inventions/](https://history-computer.com/john-von-neumann-biography-history-and-inventions/)

# Utilities used:

My personal preferance is to use locally installed apps for design works, as I take my dev machine with me places, and do not always have internet to access internet based web applications for design work.  These applications can all be installed locally, although some can be available via internet services.

## Mind Mapping

| Tool | Description | Project link | Tutorials | Windows package sources | macOS package sources | Linux package sources | Source code Repository |
----- | ----- | ----- | ----- | ----- | ----- | ----- | -----
| vym | QT based Mind Mapping tool | http://www.insilmaril.de/vym/ | The project link has links to youtube tutorials | Available via project link | Available via Project Link | Available via project link | Available via project link |

## UML Tools

Note: the links for the Plant UML line below refer to the Plant UML server/service for running the code against to generate a diagram from PlantUML code.

| Tool | Description | Project link | Tutorials | Windows package sources | macOS package sources | Linux package sources | Source code Repository |
----- | ----- | ----- | ----- | ----- | ----- | ----- | -----
| PlantUML | Domain Specific Language (DSL) for describing diagramming, with server client capability | https://plantuml.com/ http://pdf.plantuml.net/PlantUML_Language_Reference_Guide_en.pdf | https://crashedmind.github.io/PlantUMLHitchhikersGuide/ | https://plantuml.com/download | https://plantuml.com/download | https://plantuml.com/download | https://plantuml.com/download |
| Umbrello  | KDE hosted UML project | https://umbrello.kde.org/  | https://umbrello.kde.org/documentation.php  | https://community.chocolatey.org/packages/umbrello | https://invent.kde.org/packaging/homebrew-kdebrew | https://snapcraft.io/umbrello | https://github.com/KDE/umbrello |
| drawio | diagram builder | https://www.diagrams.net/ | https://drawio-app.com/tutorials/ | https://community.chocolatey.org/packages/drawio | https://formulae.brew.sh/cask/drawio | https://snapcraft.io/drawio | https://github.com/jgraph/drawio-desktop |

## .md files

| Tool | Description | Project link | Tutorials | Windows package sources | macOS package sources | Linux package sources |
----- | ----- | ----- | ----- | ----- | ----- | -----
| Vim  |  |  | 
| Intellij Idea |  |  |  |

## State Diagrams

| Tool | Description | Project link | Tutorials | Windows package sources | macOS package sources | Linux package sources |
----- | ----- | ----- | ----- | ----- | ----- | -----
| drawio | diagram builder | https://www.diagrams.net/ | https://drawio-app.com/tutorials/ | https://community.chocolatey.org/packages/drawio | https://formulae.brew.sh/cask/drawio | https://snapcraft.io/drawio | https://github.com/jgraph/drawio-desktop |

## Personal git server

| Tool | Description | Project link | Tutorials | Windows package sources | macOS package sources | Linux package sources |
----- | ----- | ----- | ----- | ----- | ----- | -----
| gogs | Personal git server | https://github.com/gogs/gogs | | | |

## 


 
 
