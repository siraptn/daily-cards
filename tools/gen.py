SANS="'Plus Jakarta Sans','Noto Sans Thai',system-ui,sans-serif"
SERIF="'Instrument Serif',Georgia,serif"
F=SANS
def page(title, inner):
    return f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title></head><body><x-dc><helmet></helmet>{inner}</x-dc></body></html>'
def footer(): pass
