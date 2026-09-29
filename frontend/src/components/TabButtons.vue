<template>
	<div class="flex p-1 bg-[#04161a] rounded-xl border border-[#D4AF37]/35 shadow-inner">
		<button
			v-for="button in buttons"
			:key="button.key ?? button.label ?? button"
			class="py-2.5 transition-all rounded-lg flex-auto text-xs sm:text-sm text-center"
			:class="
				modelValue === (button.key ?? button.label ?? button)
					? 'bg-[#0c3742] text-[#D4AF37] font-bold border border-[#D4AF37]/50 shadow-md'
					: 'text-slate-200 hover:text-white font-medium'
			"
			@click="$emit('update:modelValue', button.key ?? button.label ?? button)"
		>
			{{ button.label ?? __(button) }}
		</button>
	</div>
</template>

<script setup>
const props = defineProps({
	buttons: {
		type: Array,
		required: true,
	},
	modelValue: {
		type: String,
	},
})

defineEmits(["update:modelValue"])
</script>
