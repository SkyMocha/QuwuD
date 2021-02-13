using HarmonyLib;
using XRL;
using uwu;

// Patches the in-game text with the custom UwU generator
namespace skymocha.HarmonyPatches {

    [HarmonyPatch(typeof(XRL.Messages.MessageQueue))]
    class TextPatch01
    {

        [HarmonyPrefix]
        [HarmonyPatch("Add")]
        static void Prefix(ref string Message)
        {
            XRL.Core.XRLCore.Log("BLAH Prefix was called");
            Message = UwUGen.generate(Message);
        }
    }
}