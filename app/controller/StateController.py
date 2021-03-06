from app.controller.ScheduleController import CreateScheduleController
from app.controller.ScheduleController import CreatePlayoffsController
from app.controller.OffseasonController import StartOffseasonController
from app.domain.Phase import Phase
from app.domain.schedule.Schedule import Schedule
from app.domain.schedule.Playoff import Playoff
from app.domain.State import State
from app.server import query
from app.server import db


def VerifyState(state):
    gamesLeft = query(Schedule).filter_by(result=None).all()
    playoffsLeftList = query(Playoff).filter_by(result=None).all()
    playoffsLeft = False
    # ignore the bye weeks
    for playoff in playoffsLeftList:
        if playoff.game is not None:
            playoffsLeft = True
            break

    if state is None:
        newGamePhase = query(Phase).filter_by(phase="NEWGAME").first()
        state = State(newGamePhase, None)
        db.session.add(state)
        db.session.commit()
    elif state.team is not None and state.phase.phase == "GENERATE_SCHEDULE":
        state = CreateScheduleController()
    elif len(gamesLeft) == 0 and state.phase.phase == "REGULARSEASON":
        state.advancePhase()
        db.session.commit()
        state = CreatePlayoffsController()
    elif not playoffsLeft and state.phase.phase == "POSTSEASON":
        state.advancePhase()
        StartOffseasonController()
        db.session.commit()
    elif state.phase.phase == "COMPLETEOFFSEASON":
        startOver = query(Phase).filter_by(phase="GENERATE_SCHEDULE").first()
        state.phase = startOver
        db.session.commit()
        state = CreateScheduleController()
    return state
