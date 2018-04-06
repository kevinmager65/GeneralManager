from app.domain.State import State
from app.domain.Schedule import CreateSchedule
from app.server import query
from app.server import db


def CreateScheduleController(teams=None):
    state = query(State).first()

    if state.phase.phase != "GENERATE_SCHEDULE":
        raise Exception("Can not generate schedule during {}".format(state.phase.phase))

    create = CreateSchedule()
    create.createRegularSeasonSchedule(teams)
    state.advancePhase()
    db.session.commit()
    return state


def CreatePlayoffsController():
    state = query(State).first()

    if state.phase.phase != "STARTPOSTSEASON":
        raise Exception("Can not start playoffs during {}".format(state.phase.phase))

    create = CreateSchedule()
    create.advancePostSeasonSchedule()
    state.advancePhase()
    db.session.commit()
    return state


