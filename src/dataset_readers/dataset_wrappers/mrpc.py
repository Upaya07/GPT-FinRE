from src.utils.misc import App
from src.dataset_readers.dataset_wrappers.base_dsw import *
import logging

logger = logging.getLogger(__name__)
field_getter = App()


@field_getter.add("q")
def get_q(entry):
    return entry["sentence"]


@field_getter.add("qa")
def get_qa(entry):
    return "{sentence1} Can we say \"{sentence2}\"? {label}".format(
            sentence1=entry["sentence"],
            label=get_a(entry),
            sentence2=entry["relation"]
            )


@field_getter.add("a")
def get_a(entry):
    # print (entry,"!!!!!!!\n\n\n")
    return entry["relation"]


@field_getter.add("gen_a")
def get_gen_a(entry):
    # hypothesis, premise = get_q(entry)
    return "{ice_prompt}{sentence1} Can we say \"{sentence2}\"? ".format(
            ice_prompt="{ice_prompt}",
            sentence1=entry["sentence"],
            sentence2=entry["relation"])


@field_getter.add("choices")
def get_choices(entry):
    return ["No", "Yes"]


class DatasetWrapper(ABC):
    name = "mrpc"
    ice_separator = "\n"
    question_field = ["sentence"]
    answer_field = "relation"
    hf_dataset = "pawan2411/kdf_dev2"
    hf_dataset_name = None
    field_getter = field_getter
